"""Checkpoint Round behaviour class."""

from typing import cast
from textwrap import dedent

from aea_ledger_ethereum import Address

from packages.lstolas.skills.lst_skill.events_processing import EventsPayload
from packages.lstolas.skills.lst_skill.behaviours_classes.base_behaviour import (
    BaseState,
    LstabciappEvents,
    LstabciappStates,
)


class CheckpointRound(BaseState):
    """This class implements the behaviour of the state CheckpointRound."""

    _state = LstabciappStates.CHECKPOINTROUND
    callable_staking_proxies: list[Address] = []

    def act(self) -> None:
        """Perform the act."""
        self.log.info("Creating checkpoint...")
        while self.callable_staking_proxies:
            current_staking_proxy = self.callable_staking_proxies.pop()
            if not self.tx_settler.build_and_settle_transaction(
                contract_address=current_staking_proxy,
                function=self.strategy.lst_staking_token_locked.checkpoint,
                ledger_api=self.strategy.layer_2_api,
            ):
                self.log.error("Transaction failed to be sent...")
                self._event = LstabciappEvents.FATAL_ERROR
                self._is_done = True
                return
        self._is_done = True
        self._event = LstabciappEvents.DONE

    def is_triggered(self) -> bool:
        """Check whether the behaviour is triggered."""
        current_block_ts = int(self.strategy.layer_2_api.api.eth.get_block("latest").timestamp)  # type: ignore
        raw_events = self.strategy.lst_staking_manager_contract.get_staked_events(
            self.strategy.layer_2_api,
            self.strategy.lst_staking_manager_address,
            from_block=self.strategy.layer_2_starting_block,
        )

        all_events = EventsPayload(dictionary=raw_events)

        unique_staking_proxies = {event.args.stakingProxy for event in all_events.events}

        for staking_proxy in unique_staking_proxies:
            if not self.strategy.lst_staking_token_locked.get_num_service_ids(
                self.strategy.layer_2_api,
                staking_proxy,
            ).get("int"):
                continue
            last_checkpoint = cast(
                int,
                self.strategy.lst_staking_token_locked.ts_checkpoint(
                    self.strategy.layer_2_api,
                    staking_proxy,
                ).get("int"),
            )
            liveness_period = cast(
                int,
                self.strategy.lst_staking_token_locked.liveness_period(
                    self.strategy.layer_2_api,
                    staking_proxy,
                ).get("int"),
            )

            if current_block_ts - last_checkpoint > liveness_period:
                self.log.info(
                    dedent(
                        f"""Checkpoint needed for staking proxy {staking_proxy}.
                        Last checkpoint at  `{last_checkpoint}`.
                        Liveness period is  `{liveness_period}` seconds.
                        Current time is     `{current_block_ts}`."""
                    )
                )
                self.callable_staking_proxies.append(staking_proxy)
        return len(self.callable_staking_proxies) > 0
