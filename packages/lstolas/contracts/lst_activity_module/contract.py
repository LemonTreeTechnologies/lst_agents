"""This module contains the scaffold contract definition."""

# ruff: noqa: PLR0904
from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstActivityModule(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def default_activity(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'default_activity' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.DEFAULT_ACTIVITY().call()
        return {"int": result}

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
    def activity_nonce(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'activity_nonce' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.activityNonce().call()
        return {"int": result}

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
    def multi_send(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'multi_send' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.multiSend().call()
        return {"address": result}

    @classmethod
    def multisig(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'multisig' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.multisig().call()
        return {"address": result}

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
    def service_id(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'service_id' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.serviceId().call()
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
    def staking_proxy(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'staking_proxy' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.stakingProxy().call()
        return {"address": result}

    @classmethod
    def claim(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'claim' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.claim()

    @classmethod
    def drain(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'drain' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.drain()

    @classmethod
    def increase_initial_activity(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'increase_initial_activity' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.increaseInitialActivity()

    @classmethod
    def initialize(
        cls, ledger_api: LedgerApi, contract_address: str, multisig: Address, staking_proxy: Address, service_id: int
    ) -> JSONLike:
        """Handler method for the 'initialize' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.initialize(_multisig=multisig, _serviceId=service_id, _stakingProxy=staking_proxy)

    @classmethod
    def get_activity_increased_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        activity_change: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'ActivityIncreased' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("activityChange", activity_change)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.ActivityIncreased().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_drained_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        balance: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Drained' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("balance", balance)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Drained().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }
