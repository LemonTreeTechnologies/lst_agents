"""Claim reward tokens round behaviour."""

from typing import Any

from web3.exceptions import ContractLogicError, ContractCustomError
from aea_ledger_ethereum import Address

from packages.lstolas.skills.lst_skill.events_processing import EventsPayload
from packages.lstolas.skills.lst_skill.behaviours_classes.base_behaviour import (
    BaseState,
    LstabciappEvents,
    LstabciappStates,
)


class ClaimRewardTokensRound(BaseState):
    """This class implements the behaviour of the state ClaimRewardTokensRound."""

    _state = LstabciappStates.CLAIMREWARDTOKENSROUND
    claimable_activity_modules: list[Address] = []

    def act(self) -> None:
        """Perform the act."""
        self.log.info("Claiming reward tokens...")
        while self.claimable_activity_modules:
            contract_address = self.claimable_activity_modules.pop()
            if not self.tx_settler.build_and_settle_transaction(
                contract_address=contract_address,
                function=self.strategy.lst_activity_module_contract.claim,
                ledger_api=self.strategy.layer_2_api,
            ):
                self.log.error("Transaction failed to be sent...")
                self._event = LstabciappEvents.FATAL_ERROR
                self._is_done = True
                return
        self._event = LstabciappEvents.DONE
        self._is_done = True

    def is_triggered(self) -> bool:
        """Check whether the behaviour is triggered."""
        raw_events = self.strategy.lst_staking_manager_contract.get_staked_events(
            self.strategy.layer_2_api,
            self.strategy.lst_staking_manager_address,
            from_block=self.strategy.layer_2_starting_block,
        )

        all_events = EventsPayload(dictionary=raw_events)
        unique_staking_proxies = set()
        service_id_to_activity_module = {}

        for event in all_events.events:
            unique_staking_proxies.add(event.args.stakingProxy)
            service_id_to_activity_module[event.args.serviceId] = event.args.activityModule
        for service_id, activity_module in service_id_to_activity_module.items():
            self.log.debug(
                f"Checking claimable rewards for service ID {service_id} and activity module {activity_module}..."
            )
            function: Any = self.strategy.lst_activity_module_contract.claim(
                ledger_api=self.strategy.layer_2_api,
                contract_address=activity_module,
            )
            try:
                function.call()
                self.log.info(f"Able to call claim rewards for service ID {service_id}.")
                self.claimable_activity_modules.append(activity_module)
            except (ContractLogicError, ContractCustomError):
                self.log.debug(f"No claimable rewards for service ID {service_id}.")

        return len(self.claimable_activity_modules) > 0
