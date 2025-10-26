"""This module contains the scaffold contract definition."""

# ruff: noqa: PLR0904
from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstDistributor(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def max_lock_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_lock_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.MAX_LOCK_FACTOR().call()
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
    def lock(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'lock' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.lock().call()
        return {"address": result}

    @classmethod
    def lock_factor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'lock_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.lockFactor().call()
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
    def st(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'st' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.st().call()
        return {"address": result}

    @classmethod
    def change_implementation(
        cls, ledger_api: LedgerApi, contract_address: str, new_implementation: Address
    ) -> JSONLike:
        """Handler method for the 'change_implementation' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeImplementation(newImplementation=new_implementation)

    @classmethod
    def change_lock_factor(cls, ledger_api: LedgerApi, contract_address: str, new_lock_factor: int) -> JSONLike:
        """Handler method for the 'change_lock_factor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeLockFactor(newLockFactor=new_lock_factor)

    @classmethod
    def change_owner(cls, ledger_api: LedgerApi, contract_address: str, new_owner: Address) -> JSONLike:
        """Handler method for the 'change_owner' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeOwner(newOwner=new_owner)

    @classmethod
    def distribute(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'distribute' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.distribute()

    @classmethod
    def initialize(cls, ledger_api: LedgerApi, contract_address: str, lock_factor: int) -> JSONLike:
        """Handler method for the 'initialize' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.initialize(_lockFactor=lock_factor)

    @classmethod
    def get_distributed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address = None,
        st: Address = None,
        olas_amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Distributed' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("account", account), ("st", st), ("olasAmount", olas_amount))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Distributed().get_logs(
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
    def get_lock_factor_updated_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        lock_factor: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'LockFactorUpdated' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("lockFactor", lock_factor)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.LockFactorUpdated().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_locked_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        account: Address = None,
        olas_amount: int | None = None,
        lock_amount: int | None = None,
        vault_balance: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Locked' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("account", account),
                ("olasAmount", olas_amount),
                ("lockAmount", lock_amount),
                ("vaultBalance", vault_balance),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Locked().get_logs(fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters)
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
