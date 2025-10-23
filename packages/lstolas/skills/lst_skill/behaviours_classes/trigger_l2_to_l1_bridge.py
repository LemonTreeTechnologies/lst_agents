"""Trigger the bridge from L2 to L1 if there are pending transfers."""

from enum import Enum
from typing import cast
from datetime import datetime

from pydantic import BaseModel
from aea_ledger_ethereum import Address

from packages.lstolas.skills.lst_skill.behaviours_classes.base_behaviour import (
    BaseState,
    LstabciappEvents,
    LstabciappStates,
)


TX_MINING_TIMEOUT = 300  # seconds


class TriggerOperations(Enum):
    """Enum for the different operations that can trigger the bridge."""

    REWARD = "0x0b9821ae606ebc7c79bf3390bdd3dc93e1b4a7cda27aad60646e7b88ff55b001"
    UNSTAKE = "0x8ca9a95e41b5eece253c93f5b31eed1253aed6b145d8a6e14d913fdf8e732293"
    UNSTAKE_RETIRED = "0x9065ad15d9673159e4597c86084aff8052550cec93c5a6e44b3f1dba4c8731b3"


class BalanceResponse(BaseModel):
    """Response model for the balance of an operation."""

    balance: int
    receiver: Address


class TriggerL2ToL1BridgeRound(BaseState):
    """This class implements the behaviour of the state TriggerL2ToL1BridgeRound."""

    _state = LstabciappStates.TRIGGERL2TOL1BRIDGEROUND
    current_operation: TriggerOperations | None = None
    current_balance: BalanceResponse | None = None
    last_run_datetime: datetime | None = None

    def act(self) -> None:
        """Perform the act."""
        if self.current_operation is None or self.current_balance is None:
            self.log.error("Current operation or balance is not set.")
            self._event = LstabciappEvents.FATAL_ERROR
            self._is_done = True
            return
        self.log.info("Triggering L2 to L1 bridge...")

        if not self.tx_settler.build_and_settle_transaction(
            contract_address=self.strategy.lst_collector_address,
            function=self.strategy.lst_collector_contract.relay_tokens,
            ledger_api=self.strategy.layer_2_api,
            operation=self.current_operation.value,  # type: ignore
            bridge_payload="0x",
        ):
            self._event = LstabciappEvents.FATAL_ERROR
        else:
            self._event = LstabciappEvents.DONE
        self._is_done = True
        self.last_run_datetime = datetime.utcnow()  # noqa: DTZ003

    def has_already_run_today(self) -> bool:
        """Check if the behaviour has run today.
        Only trigger after 02:00 UTC.
        """
        if self.last_run_datetime is None:
            return False
        now_utc = datetime.utcnow()  # noqa: DTZ003
        return bool(now_utc.date() == self.last_run_datetime.date() and now_utc.hour >= 2)

    def is_triggered(self) -> bool:
        """Check if the state is triggered."""
        if self.has_already_run_today():
            self.log.info("Bridge has already been triggered today, skipping.")
            return False
        self.current_balance, self.current_operation = None, None
        min_olas_balance = self.get_min_olas_balance()
        if not min_olas_balance:
            self.log.warning("No minimal OLAS balance set, skipping bridge trigger.")
            return False

        for operation in TriggerOperations:
            operation_balance = self.get_operation_balance(operation)
            if operation_balance.balance >= min_olas_balance:
                self.log.info(f"Operation {operation} triggered with balance of {operation_balance.balance}.")
                self.current_operation = operation
                self.current_balance = operation_balance
                return True
            self.log.debug(f"Operation {operation} has insufficient balance {operation_balance}.")
        return False

    def get_min_olas_balance(self) -> int:
        """Get the minimal balance to trigger the bridge."""
        return cast(
            int,
            self.strategy.lst_collector_contract.min_olas_balance(
                self.strategy.layer_2_api, self.strategy.lst_collector_address
            ).get("int"),
        )

    def get_operation_balance(self, operation: TriggerOperations) -> BalanceResponse:
        """Get the balance for a specific operation."""
        data = self.strategy.lst_collector_contract.map_operation_receiver_balances(
            self.strategy.layer_2_api, self.strategy.lst_collector_address, operation.value
        )
        return BalanceResponse(balance=cast(int, data.get("balance")), receiver=cast(Address, data.get("receiver")))
