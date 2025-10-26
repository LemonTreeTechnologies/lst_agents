"""This module contains the scaffold contract definition."""
# ruff: noqa: PLR0904

from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstCollector(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def max_protocol_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_protocol_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.MAX_PROTOCOL_FACTOR().call()
        return {"int": result}

    @classmethod
    def min_olas_balance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'min_olas_balance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.MIN_OLAS_BALANCE().call()
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
    def reward(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'reward' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.REWARD().call()
        return {"str": result}

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
    def map_operation_receiver_balances(cls, ledger_api: LedgerApi, contract_address: str, var_0: str) -> JSONLike:
        """Handler method for the 'map_operation_receiver_balances' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapOperationReceiverBalances(var_0).call()
        return {"balance": result[0], "receiver": result[1]}

    @classmethod
    def map_staking_proxy_unstake_reserves(
        cls, ledger_api: LedgerApi, contract_address: str, var_0: Address
    ) -> JSONLike:
        """Handler method for the 'map_staking_proxy_unstake_reserves' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.mapStakingProxyUnstakeReserves(var_0).call()
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
    def protocol_balance(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'protocol_balance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.protocolBalance().call()
        return {"int": result}

    @classmethod
    def protocol_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'protocol_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.protocolFactor().call()
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
    def change_protocol_factor(cls, ledger_api: LedgerApi, contract_address: str, new_protocol_factor: int) -> JSONLike:
        """Handler method for the 'change_protocol_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeProtocolFactor(newProtocolFactor=new_protocol_factor)

    @classmethod
    def change_staking_manager(
        cls, ledger_api: LedgerApi, contract_address: str, new_staking_manager: Address
    ) -> JSONLike:
        """Handler method for the 'change_staking_manager' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeStakingManager(newStakingManager=new_staking_manager)

    @classmethod
    def change_staking_processor_l2(
        cls, ledger_api: LedgerApi, contract_address: str, new_staking_processor_l2: Address
    ) -> JSONLike:
        """Handler method for the 'change_staking_processor_l2' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeStakingProcessorL2(newStakingProcessorL2=new_staking_processor_l2)

    @classmethod
    def fund_external(cls, ledger_api: LedgerApi, contract_address: str, account: Address, amount: int) -> JSONLike:
        """Handler method for the 'fund_external' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.fundExternal(account=account, amount=amount)

    @classmethod
    def initialize(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'initialize' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.initialize()

    @classmethod
    def rebalance_from_unstake_reserve(
        cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address, amount: int, operation: str
    ) -> JSONLike:
        """Handler method for the 'rebalance_from_unstake_reserve' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.rebalanceFromUnstakeReserve(
            amount=amount, operation=operation, stakingProxy=staking_proxy
        )

    @classmethod
    def relay_tokens(
        cls, ledger_api: LedgerApi, contract_address: str, operation: str, bridge_payload: str
    ) -> JSONLike:
        """Handler method for the 'relay_tokens' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.relayTokens(bridgePayload=bridge_payload, operation=operation)

    @classmethod
    def set_operation_receivers(
        cls, ledger_api: LedgerApi, contract_address: str, operations: list[str], receivers: list[Address]
    ) -> JSONLike:
        """Handler method for the 'set_operation_receivers' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.setOperationReceivers(operations=operations, receivers=receivers)

    @classmethod
    def top_up_balance(cls, ledger_api: LedgerApi, contract_address: str, amount: int, operation: str) -> JSONLike:
        """Handler method for the 'top_up_balance' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.topUpBalance(amount=amount, operation=operation)

    @classmethod
    def top_up_unstake_reserve(
        cls, ledger_api: LedgerApi, contract_address: str, staking_proxy: Address, amount: int
    ) -> JSONLike:
        """Handler method for the 'top_up_unstake_reserve' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.topUpUnstakeReserve(amount=amount, stakingProxy=staking_proxy)

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
    def get_operation_receiver_balances_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        operation: str | None = None,
        receiver: Address = None,
        balance: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'OperationReceiverBalancesUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("operation", operation), ("receiver", receiver), ("balance", balance))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.OperationReceiverBalancesUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_operation_receivers_set_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        operations: list[str] | None = None,
        receivers: list[Address] | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'OperationReceiversSet' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value for key, value in (("operations", operations), ("receivers", receivers)) if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.OperationReceiversSet().get_logs(
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
    def get_protocol_balance_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        protocol_balance: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ProtocolBalanceUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("protocolBalance", protocol_balance)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ProtocolBalanceUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_protocol_factor_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        protocol_factor: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ProtocolFactorUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("protocolFactor", protocol_factor)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ProtocolFactorUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_manager_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        staking_manager: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingManagerUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("stakingManager", staking_manager)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingManagerUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_processor_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        staking_processor_l2: Address = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingProcessorUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("stakingProcessorL2", staking_processor_l2)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingProcessorUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_proxy_unstake_reserve_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        sender: Address = None,
        staking_proxy: Address = None,
        amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingProxyUnstakeReserveUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("sender", sender), ("stakingProxy", staking_proxy), ("amount", amount))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingProxyUnstakeReserveUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_tokens_relayed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        l1_distributor: Address = None,
        amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'TokensRelayed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value for key, value in (("l1Distributor", l1_distributor), ("amount", amount)) if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.TokensRelayed().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }
