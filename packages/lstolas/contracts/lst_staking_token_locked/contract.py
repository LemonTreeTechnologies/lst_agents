"""This module contains the scaffold contract definition."""

# ruff: noqa: PLR0904
from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstStakingTokenLocked(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def version(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'version' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.VERSION().call()
        return {"str": result}

    @classmethod
    def activity_checker(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'activity_checker' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.activityChecker().call()
        return {"address": result}

    @classmethod
    def available_rewards(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'available_rewards' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.availableRewards().call()
        return {"int": result}

    @classmethod
    def balance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'balance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.balance().call()
        return {"int": result}

    @classmethod
    def calculate_staking_last_reward(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'calculate_staking_last_reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.calculateStakingLastReward(serviceId=service_id).call()
        return {"reward": result}

    @classmethod
    def calculate_staking_reward(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'calculate_staking_reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.calculateStakingReward(serviceId=service_id).call()
        return {"reward": result}

    @classmethod
    def emissions_amount(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'emissions_amount' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.emissionsAmount().call()
        return {"int": result}

    @classmethod
    def epoch_counter(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'epoch_counter' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.epochCounter().call()
        return {"int": result}

    @classmethod
    def get_next_reward_checkpoint_timestamp(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_next_reward_checkpoint_timestamp' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getNextRewardCheckpointTimestamp().call()
        return {"tsNext": result}

    @classmethod
    def get_num_service_ids(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_num_service_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getNumServiceIds().call()
        return {"int": result}

    @classmethod
    def get_service_ids(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_service_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getServiceIds().call()
        return {"list[int]": result}

    @classmethod
    def get_service_info(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'get_service_info' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getServiceInfo(serviceId=service_id).call()
        return {"sInfo": result}

    @classmethod
    def get_staking_state(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'get_staking_state' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getStakingState(serviceId=service_id).call()
        return {"stakingState": result}

    @classmethod
    def liveness_period(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'liveness_period' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.livenessPeriod().call()
        return {"int": result}

    @classmethod
    def map_service_info(cls, ledger_api: LedgerApi, contract_address: str, var_0: int) -> JSONLike:
        """Handler method for the 'map_service_info' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapServiceInfo(var_0).call()
        return {"multisig": result[0], "owner": result[1], "tsStart": result[2], "reward": result[3]}

    @classmethod
    def max_num_services(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_num_services' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.maxNumServices().call()
        return {"int": result}

    @classmethod
    def min_staking_deposit(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'min_staking_deposit' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.minStakingDeposit().call()
        return {"int": result}

    @classmethod
    def rewards_per_second(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'rewards_per_second' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.rewardsPerSecond().call()
        return {"int": result}

    @classmethod
    def service_registry(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'service_registry' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.serviceRegistry().call()
        return {"address": result}

    @classmethod
    def service_registry_token_utility(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'service_registry_token_utility' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.serviceRegistryTokenUtility().call()
        return {"address": result}

    @classmethod
    def set_service_ids(cls, ledger_api: LedgerApi, contract_address: str, var_0: int) -> JSONLike:
        """Handler method for the 'set_service_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.setServiceIds(var_0).call()
        return {"int": result}

    @classmethod
    def staking_manager(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'staking_manager' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.stakingManager().call()
        return {"address": result}

    @classmethod
    def staking_token(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'staking_token' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.stakingToken().call()
        return {"address": result}

    @classmethod
    def time_for_emissions(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'time_for_emissions' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.timeForEmissions().call()
        return {"int": result}

    @classmethod
    def ts_checkpoint(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'ts_checkpoint' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.tsCheckpoint().call()
        return {"int": result}

    @classmethod
    def checkpoint(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'checkpoint' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.checkpoint()

    @classmethod
    def claim(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'claim' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.claim(serviceId=service_id)

    @classmethod
    def deposit(cls, ledger_api: LedgerApi, contract_address: str, amount: int) -> JSONLike:
        """Handler method for the 'deposit' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.deposit(amount=amount)

    @classmethod
    def initialize(cls, ledger_api: LedgerApi, contract_address: str, staking_params: tuple) -> JSONLike:
        """Handler method for the 'initialize' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.initialize(_stakingParams=staking_params)

    @classmethod
    def on_e_r_c721_received(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address, var_1: Address, var_2: int, var_3: str
    ) -> JSONLike:
        """Handler method for the 'on_e_r_c721_received' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.onERC721Received(var_0, var_1, var_2, var_3)

    @classmethod
    def stake(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'stake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.stake(serviceId=service_id)

    @classmethod
    def unstake(cls, ledger_api: LedgerApi, contract_address: str, service_id: int) -> JSONLike:
        """Handler method for the 'unstake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.unstake(serviceId=service_id)

    @classmethod
    def get_checkpoint_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        epoch: int | None = None,
        available_rewards: int | None = None,
        service_ids: list[int] | None = None,
        rewards: list[int] | None = None,
        epoch_length: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Checkpoint' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("epoch", epoch),
                ("availableRewards", available_rewards),
                ("serviceIds", service_ids),
                ("rewards", rewards),
                ("epochLength", epoch_length),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Checkpoint().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_deposit_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        sender: Address = None,
        amount: int | None = None,
        balance: int | None = None,
        available_rewards: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Deposit' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("sender", sender),
                ("amount", amount),
                ("balance", balance),
                ("availableRewards", available_rewards),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Deposit().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_reward_claimed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        epoch: int | None = None,
        service_id: int | None = None,
        owner: Address = None,
        multisig: Address = None,
        nonces: list[int] | None = None,
        reward: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'RewardClaimed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("epoch", epoch),
                ("serviceId", service_id),
                ("owner", owner),
                ("multisig", multisig),
                ("nonces", nonces),
                ("reward", reward),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.RewardClaimed().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_service_staked_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        epoch: int | None = None,
        service_id: int | None = None,
        owner: Address = None,
        multisig: Address = None,
        nonces: list[int] | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ServiceStaked' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("epoch", epoch),
                ("serviceId", service_id),
                ("owner", owner),
                ("multisig", multisig),
                ("nonces", nonces),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ServiceStaked().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_service_unstaked_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        epoch: int | None = None,
        service_id: int | None = None,
        owner: Address = None,
        multisig: Address = None,
        nonces: list[int] | None = None,
        reward: int | None = None,
        available_rewards: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ServiceUnstaked' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("epoch", epoch),
                ("serviceId", service_id),
                ("owner", owner),
                ("multisig", multisig),
                ("nonces", nonces),
                ("reward", reward),
                ("availableRewards", available_rewards),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ServiceUnstaked().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_withdraw_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        to: Address = None,
        amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Withdraw' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("to", to), ("amount", amount)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Withdraw().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }
