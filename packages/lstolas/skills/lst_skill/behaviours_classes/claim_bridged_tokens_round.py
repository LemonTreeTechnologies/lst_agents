"""FinalizeBridgedTokensRound class module."""

from typing import cast

from pydantic import BaseModel
from eth_utils.abi import event_abi_to_log_topic
from web3.exceptions import ContractLogicError
from web3._utils.events import get_event_data  # noqa: PLC2701
from aea_ledger_ethereum import HexBytes
from eth_utils.conversions import to_hex

from packages.lstolas.skills.lst_skill.events_processing import Event, EventsPayload, hexify
from packages.lstolas.skills.lst_skill.behaviours_classes.base_behaviour import (
    BaseState,
    LstabciappEvents,
    LstabciappStates,
)


class PendingClaim(BaseModel):
    """Model for a pending claim."""

    data: str
    signatures: str


class ClaimBridgedTokensRound(BaseState):
    """This class implements the behaviour of the state FinalizeBridgedTokensRound."""

    _state = LstabciappStates.CLAIMBRIDGEDTOKENSROUND
    pending_claims: list[PendingClaim] = []

    def act(self) -> None:
        """Perform the act."""
        self.log.info("Claiming bridged tokens...")

        while self.pending_claims:
            claim = self.pending_claims.pop(0)
            self.log.info("Finalizing claim...")
            self.log.info(f"Data: {claim.data}")
            self.log.info(f"Signatures: {claim.signatures}")
            if not self.tx_settler.build_and_settle_transaction(
                contract_address=self.strategy.layer_1_amb_home,
                function=self.strategy.amb_mainnet_contract.execute_signatures,
                ledger_api=self.strategy.layer_1_api,
                data=claim.data,
                signatures=claim.signatures,
            ):
                self.log.error("Transaction failed to be sent...")
                self._event = LstabciappEvents.FATAL_ERROR
                self._is_done = True
                return
        self._event = LstabciappEvents.DONE
        self._is_done = True

    def is_triggered(self) -> bool:
        """Check if the state is triggered."""
        # we check if there are bridged tokens to be finalised here;
        pending_bridges = {}

        events = EventsPayload(
            dictionary=self.strategy.lst_collector_contract.get_tokens_relayed_events(
                self.strategy.layer_2_api, self.strategy.lst_collector_address, from_block=17590111
            ),
        )
        l2_to_l1_events = {}
        for event in events.events:
            individual_events = self._decode_event_data(event)
            for individual_event in individual_events:
                l2_to_l1_events[individual_event.args.messageId] = individual_event

        # we now check if there are any events to be processed
        self.log.debug(f"Found {len(l2_to_l1_events)} L2 to L1 events.")
        self.log.debug("Checking for any events to be finalized...")
        for message_id in l2_to_l1_events:  # noqa: PLC0206
            # check if the event has been processed on the layer 1
            # we search for events on the l1 for the same message id
            l1_events = EventsPayload(
                dictionary=self.strategy.amb_mainnet_contract.get_relayed_message_events(
                    self.strategy.layer_1_api,
                    self.strategy.layer_1_amb_home,
                    from_block=9123229,
                    message_id=message_id,
                ),
            )

            # sleep to avoid silly rate limits
            if not l1_events.events:
                self.log.info(f"No L1 event found for message id {message_id}. It is pending.")
                pending_bridges[message_id] = l2_to_l1_events[message_id]
        # we now check if the bridge can be finalized
        for message_id, event in pending_bridges.items():
            try:
                signature = cast(
                    HexBytes,
                    self.strategy.layer_2_amb_helper_contract.get_signatures(
                        self.strategy.layer_2_api, self.strategy.layer_2_amb_helper, event.args.encodedData
                    )["str"],
                ).hex()
                if signature and len(signature) > 2:
                    self.log.info(f"Bridge can be finalized for message id {message_id}.")
                    self.pending_claims.append(
                        PendingClaim(
                            data=event.args.encodedData,
                            signatures="0x" + signature,
                        )
                    )
            except ContractLogicError as e:
                self.log.debug(f"Error while fetching signatures: {e}")
                continue
        return len(self.pending_claims) > 0

    def _decode_event_data(self, event: Event) -> list:
        """Decode the events data.
        1. get the transaction receipt.
        2. get the message hash from the event.

        """
        receipt = self.strategy.layer_2_api.api.eth.get_transaction_receipt(event["transactionHash"])
        amb_abi = self.load_abi(self.strategy.layer_2_amb_home_contract)
        event_abis = [a for a in amb_abi if a.get("type") == "event"]
        topic_to_eventabi = {to_hex(event_abi_to_log_topic(e)): e for e in event_abis}  # pyright: ignore
        raw_logs = [log for log in receipt["logs"] if log["address"].lower() == self.strategy.layer_2_amb_home.lower()]
        decoded_events = []
        for raw_log in raw_logs:
            event_abi = topic_to_eventabi[to_hex(hexstr=raw_log["topics"][0].hex())]  # pyright: ignore
            decoded = get_event_data(self.strategy.layer_2_api.api.codec, event_abi, raw_log)
            decoded_events.append(hexify(decoded))
        return decoded_events
