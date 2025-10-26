"""This module contains the scaffold contract definition."""

# ruff: noqa: PLR0904
from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstStakingManager(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def num_agent_instances(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'num_agent_instances' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.NUM_AGENT_INSTANCES().call()
        return {"int": result}

    @classmethod
    def proxy_slot(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'proxy_slot' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.PROXY_SLOT().call()
        return {"str": result}

    @classmethod
    def threshold(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'threshold' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.THRESHOLD().call()
        return {"int": result}

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
    def agent_id(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'agent_id' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.agentId().call()
        return {"int": result}

    @classmethod
    def beacon(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'beacon' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.beacon().call()
        return {"address": result}

    @classmethod
    def collector(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'collector' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.collector().call()
        return {"address": result}

    @classmethod
    def config_hash(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'config_hash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.configHash().call()
        return {"str": result}

    @classmethod
    def fallback_handler(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'fallback_handler' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.fallbackHandler().call()
        return {"address": result}

    @classmethod
    def get_staked_service_ids(cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address) -> JSONLike:
        """Handler method for the 'get_staked_service_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getStakedServiceIds(stakingProxy=staking_proxy).call()
        return {"serviceIds": result}

    @classmethod
    def l2_staking_processor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'l2_staking_processor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.l2StakingProcessor().call()
        return {"address": result}

    @classmethod
    def map_last_staked_service_idxs(cls, ledger_api: LedgerApi, contract_address: str, var_0: Address) -> JSONLike:
        """Handler method for the 'map_last_staked_service_idxs' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapLastStakedServiceIdxs(var_0).call()
        return {"int": result}

    @classmethod
    def map_service_id_activity_modules(cls, ledger_api: LedgerApi, contract_address: str, var_0: int) -> JSONLike:
        """Handler method for the 'map_service_id_activity_modules' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapServiceIdActivityModules(var_0).call()
        return {"address": result}

    @classmethod
    def map_staked_service_ids(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address, var_1: int
    ) -> JSONLike:
        """Handler method for the 'map_staked_service_ids' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapStakedServiceIds(var_0, var_1).call()
        return {"int": result}

    @classmethod
    def map_staking_proxy_balances(cls, ledger_api: LedgerApi, contract_address: str, var_0: Address) -> JSONLike:
        """Handler method for the 'map_staking_proxy_balances' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapStakingProxyBalances(var_0).call()
        return {"int": result}

    @classmethod
    def olas(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'olas' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.olas().call()
        return {"address": result}

    @classmethod
    def owner(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'owner' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.owner().call()
        return {"address": result}

    @classmethod
    def safe_l2(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'safe_l2' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.safeL2().call()
        return {"address": result}

    @classmethod
    def safe_module_initializer(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'safe_module_initializer' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.safeModuleInitializer().call()
        return {"address": result}

    @classmethod
    def safe_multisig(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'safe_multisig' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.safeMultisig().call()
        return {"address": result}

    @classmethod
    def safe_same_address_multisig(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'safe_same_address_multisig' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.safeSameAddressMultisig().call()
        return {"address": result}

    @classmethod
    def service_manager(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'service_manager' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.serviceManager().call()
        return {"address": result}

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
    def staking_factory(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'staking_factory' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.stakingFactory().call()
        return {"address": result}

    @classmethod
    def change_implementation(
        cls, ledger_api: LedgerApi, contract_address: str, new_implementation: Address
    ) -> JSONLike:
        """Handler method for the 'change_implementation' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeImplementation(newImplementation=new_implementation)

    @classmethod
    def change_owner(cls, ledger_api: LedgerApi, contract_address: str, new_owner: Address) -> JSONLike:
        """Handler method for the 'change_owner' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeOwner(newOwner=new_owner)

    @classmethod
    def change_staking_processor_l2(
        cls, ledger_api: LedgerApi, contract_address: str, new_staking_processor_l2: Address
    ) -> JSONLike:
        """Handler method for the 'change_staking_processor_l2' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeStakingProcessorL2(newStakingProcessorL2=new_staking_processor_l2)

    @classmethod
    def claim(cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address, service_id: int) -> JSONLike:
        """Handler method for the 'claim' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.claim(serviceId=service_id, stakingProxy=staking_proxy)

    @classmethod
    def initialize(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        safe_multisig: Address,
        safe_same_address_multisig: Address,
        fallback_handler: Address,
    ) -> JSONLike:
        """Handler method for the 'initialize' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.initialize(
            _fallbackHandler=fallback_handler,
            _safeMultisig=safe_multisig,
            _safeSameAddressMultisig=safe_same_address_multisig,
        )

    @classmethod
    def on_e_r_c721_received(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address, var_1: Address, var_2: int, var_3: str
    ) -> JSONLike:
        """Handler method for the 'on_e_r_c721_received' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.onERC721Received(var_0, var_1, var_2, var_3)

    @classmethod
    def stake(
        cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address, amount: int, operation: str
    ) -> JSONLike:
        """Handler method for the 'stake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.stake(amount=amount, operation=operation, stakingProxy=staking_proxy)

    @classmethod
    def unstake(
        cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address, amount: int, operation: str
    ) -> JSONLike:
        """Handler method for the 'unstake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.unstake(amount=amount, operation=operation, stakingProxy=staking_proxy)

    @classmethod
    def get_claimed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        staking_proxy: Address = None,
        service_id: int | None = None,
        activity_module: Address = None,
        reward: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Claimed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("stakingProxy", staking_proxy),
                ("serviceId", service_id),
                ("activityModule", activity_module),
                ("reward", reward),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Claimed().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_created_and_deployed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        service_id: int | None = None,
        multisig: Address = None,
        activity_module: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'CreatedAndDeployed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("serviceId", service_id), ("multisig", multisig), ("activityModule", activity_module))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.CreatedAndDeployed().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_implementation_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        implementation: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ImplementationUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("implementation", implementation)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ImplementationUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_native_token_received_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'NativeTokenReceived' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("amount", amount)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.NativeTokenReceived().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_owner_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'OwnerUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("owner", owner)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.OwnerUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_re_deployed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        service_id: int | None = None,
        multisig: Address = None,
        activity_module: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ReDeployed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("serviceId", service_id), ("multisig", multisig), ("activityModule", activity_module))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ReDeployed().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staked_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        staking_proxy: Address = None,
        service_id: int | None = None,
        activity_module: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Staked' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("stakingProxy", staking_proxy),
                ("serviceId", service_id),
                ("activityModule", activity_module),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Staked().get_logs(fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters)
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_balance_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        operation: str | None = None,
        staking_proxy: Address = None,
        num_stakes: int | None = None,
        balance: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingBalanceUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("operation", operation),
                ("stakingProxy", staking_proxy),
                ("numStakes", num_stakes),
                ("balance", balance),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingBalanceUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_processor_l2_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        l2_staking_processor: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingProcessorL2Updated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("l2StakingProcessor", l2_staking_processor)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingProcessorL2Updated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_unstaked_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        staking_proxy: Address = None,
        service_id: int | None = None,
        activity_module: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Unstaked' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("stakingProxy", staking_proxy),
                ("serviceId", service_id),
                ("activityModule", activity_module),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Unstaked().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }
