"""Behaviour class for the state RedeemRound of the LstAbciApp."""

from enum import Enum

from pydantic import BaseModel

from packages.lstolas.skills.lst_skill.events_processing import EventsPayload
from packages.lstolas.skills.lst_skill.behaviours_classes.base_behaviour import (
    BaseState,
    LstabciappEvents,
    LstabciappStates,
)


class OperationStatus(Enum):
    """Status of the operation."""

    NON_EXISTENT = 0
    EXTERNAL_CALLED_FAILED = 1
    INSUFFICIENT_OLAS_BALANCE = 2
    UNSUPPORTED_OPERATION_TYPE = 3
    CONTRACT_IS_PAUSED = 4


class PendingRequest(BaseModel):
    """A pending request to be processed."""

    batch_hash: str
    target: str
    amount: int
    operation: str
    status: OperationStatus


class RedeemRound(BaseState):
    """This class implements the behaviour of the state RedeemRound."""

    _state = LstabciappStates.REDEEMROUND
    last_scanned_block: int | None = None
    last_completed_block: int | None = None

    events_to_process: list[PendingRequest] = []

    def act(self) -> None:
        """Perform the act."""
        self.log.info("Redeeming tokens...")
        succeses, failures = [], []
        while self.events_to_process:
            event = self.events_to_process.pop(0)
            self.log.info(f"Processing event with batch hash {event}...")
            if not self.tx_settler.build_and_settle_transaction(
                contract_address=self.strategy.lst_staking_processor_l2_address,
                function=self.strategy.lst_staking_processor_l2_contract.redeem,
                ledger_api=self.strategy.layer_2_api,
                batch_hash=event.batch_hash,
                target=event.target,
                amount=event.amount,
                operation=event.operation,
            ):
                self.log.error("Transaction failed to be sent...")
                failures.append(event)
            else:
                self.log.info("Transaction successfully sent.")
                succeses.append(event)
        if failures:
            self.log.info(f"{len(failures)} requests failed to be processed. They will be retried in the next round.")
            self._event = LstabciappEvents.FATAL_ERROR
        else:
            self.log.info(f"All {len(succeses)} requests were successfully processed.")
            self._event = LstabciappEvents.DONE
            self.last_completed_block = self.last_scanned_block
        self._is_done = True

    def is_triggered(self) -> bool:
        """Check if the condition is met to trigger this behaviour."""
        # we check if there are tokens to be redeemed here;
        queued_requests = EventsPayload(
            dictionary=self.strategy.lst_staking_processor_l2_contract.get_request_queued_events(
                self.strategy.layer_2_api,
                self.strategy.lst_staking_processor_l2_address,
                from_block=17590111 if self.last_completed_block is None else self.last_completed_block,
            )
        )
        self.last_scanned_block = queued_requests.to_block
        if queued_requests.events:
            self.log.info(f"Found {len(queued_requests.events)} queued requests to be processed.")
            potential_events_to_process = [
                PendingRequest(
                    batch_hash="0x" + event.args.batchHash.hex(),
                    target=event.args.target,
                    amount=event.args.amount,
                    operation="0x" + event.args.operation.hex(),
                    status=OperationStatus(event.args.status),
                )
                for event in queued_requests.events
            ]

            for event in potential_events_to_process:
                if event.status is not OperationStatus.INSUFFICIENT_OLAS_BALANCE:
                    self.log.info(
                        f"Request with batch hash {event.batch_hash} has status {event.status} and will be skipped."
                    )
                    continue
                self.send_notification_to_user(
                    title="Redeem request detected",
                    msg=f"Detected a redeem request with batch hash {event.batch_hash}. Attempting to process it.",
                )
                self.context.logger.info(f"Checking on event: {event}")

                queued_hash = (
                    self.strategy.lst_staking_processor_l2_contract.get_queued_hash(
                        self.strategy.layer_2_api,
                        self.strategy.lst_staking_processor_l2_address,
                        batch_hash=event.batch_hash,
                        target=event.target,
                        amount=event.amount,
                        operation=event.operation,
                    )
                    .get("str")
                    .hex()  # type: ignore
                )
                # we now check if the request is still queued
                is_still_queued = self.strategy.lst_staking_processor_l2_contract.queued_hashes(
                    self.strategy.layer_2_api,
                    self.strategy.lst_staking_processor_l2_address,
                    "0x" + queued_hash,
                ).get("bool")
                if is_still_queued:
                    self.events_to_process.append(event)
                    self.log.info(
                        f"Request with batch hash {event.batch_hash} is state: {is_still_queued} and will be processed."
                    )
                else:
                    self.log.info(
                        f"Request with batch hash {event.batch_hash} is no longer queued and will be skipped."
                    )
            if self.events_to_process:
                return True
        self.last_completed_block = self.last_scanned_block
        return False
