"""This module contains the scaffold contract definition."""

# ruff: noqa: PLR0904
from aea.common import JSONLike
from aea.crypto.base import Address, LedgerApi
from aea.contracts.base import Contract
from aea.configurations.base import PublicId


class LstStakingProcessorL2(Contract):
    """The scaffold contract class for a smart contract."""

    contract_id = PublicId.from_str("open_aea/scaffold:0.1.0")

    @classmethod
    def max_chain_id(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'max_chain_id' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.MAX_CHAIN_ID().call()
        return {"int": result}

    @classmethod
    def stake(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'stake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.STAKE().call()
        return {"str": result}

    @classmethod
    def unstake(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'unstake' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.UNSTAKE().call()
        return {"str": result}

    @classmethod
    def unstake_retired(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'unstake_retired' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.UNSTAKE_RETIRED().call()
        return {"str": result}

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
    def get_bridging_decimals(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'get_bridging_decimals' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getBridgingDecimals().call()
        return {"int": result}

    @classmethod
    def get_queued_hash(
        cls, ledger_api: LedgerApi, contract_address: str, batch_hash: str, target: Address, amount: int, operation: str
    ) -> JSONLike:
        """Handler method for the 'get_queued_hash' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.getQueuedHash(
            amount=amount, batchHash=batch_hash, operation=operation, target=target
        ).call()
        return {"str": result}

    @classmethod
    def l1_deposit_processor(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'l1_deposit_processor' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.l1DepositProcessor().call()
        return {"address": result}

    @classmethod
    def l1_source_chain_id(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'l1_source_chain_id' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.l1SourceChainId().call()
        return {"int": result}

    @classmethod
    def l2_message_relayer(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'l2_message_relayer' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.l2MessageRelayer().call()
        return {"address": result}

    @classmethod
    def l2_token_relayer(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'l2_token_relayer' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.l2TokenRelayer().call()
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
    def paused(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'paused' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.paused().call()
        return {"int": result}

    @classmethod
    def processed_hashes(cls, ledger_api: LedgerApi, contract_address: str, var_0: str) -> JSONLike:
        """Handler method for the 'processed_hashes' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.processedHashes(var_0).call()
        return {"bool": result}

    @classmethod
    def queued_hashes(cls, ledger_api: LedgerApi, contract_address: str, var_0: str) -> JSONLike:
        """Handler method for the 'queued_hashes' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        result = instance.functions.queuedHashes(var_0).call()
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
    def change_owner(cls, ledger_api: LedgerApi, contract_address: str, new_owner: Address) -> JSONLike:
        """Handler method for the 'change_owner' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.changeOwner(newOwner=new_owner)

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
    def pause(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'pause' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.pause()

    @classmethod
    def receive_message(cls, ledger_api: LedgerApi, contract_address: str, data: str) -> JSONLike:
        """Handler method for the 'receive_message' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.receiveMessage(data=data)

    @classmethod
    def redeem(
        cls, ledger_api: LedgerApi, contract_address: str, batch_hash: str, target: Address, amount: int, operation: str
    ) -> JSONLike:
        """Handler method for the 'redeem' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.redeem(amount=amount, batchHash=batch_hash, operation=operation, target=target)

    @classmethod
    def relay_to_l1(
        cls, ledger_api: LedgerApi, contract_address: str, to: Address, olas_amount: int, var_2: str
    ) -> JSONLike:
        """Handler method for the 'relay_to_l1' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.relayToL1(var_2, olasAmount=olas_amount, to=to)

    @classmethod
    def unpause(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
    ) -> JSONLike:
        """Handler method for the 'unpause' requests."""
        instance = cls.get_instance(ledger_api, contract_address)
        return instance.functions.unpause()

    @classmethod
    def get_drain_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        owner: Address = None,
        amount: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'Drain' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("owner", owner), ("amount", amount)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.Drain().get_logs(fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters)
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_funds_received_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        sender: Address = None,
        value: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'FundsReceived' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {key: value for key, value in (("sender", sender), ("value", value)) if value is not None}
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.FundsReceived().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_message_received_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        sender: Address = None,
        chain_id: int | None = None,
        data: str | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'MessageReceived' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (("sender", sender), ("chainId", chain_id), ("data", data))
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.MessageReceived().get_logs(
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
    def get_request_executed_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        batch_hash: str | None = None,
        target: Address = None,
        amount: int | None = None,
        operation: str | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'RequestExecuted' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("batchHash", batch_hash),
                ("target", target),
                ("amount", amount),
                ("operation", operation),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.RequestExecuted().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_request_queued_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        batch_hash: str | None = None,
        target: Address = None,
        amount: int | None = None,
        operation: str | None = None,
        status: int | None = None,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'RequestQueued' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        arg_filters = {
            key: value
            for key, value in (
                ("batchHash", batch_hash),
                ("target", target),
                ("amount", amount),
                ("operation", operation),
                ("status", status),
            )
            if value is not None
        }
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.RequestQueued().get_logs(
            fromBlock=from_block, toBlock=to_block, argument_filters=arg_filters
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_processor_paused_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingProcessorPaused' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingProcessorPaused().get_logs(
            fromBlock=from_block,
            toBlock=to_block,
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }

    @classmethod
    def get_staking_processor_unpaused_events(
        cls,
        ledger_api: LedgerApi,
        contract_address: str,
        look_back: int = 1000,
        to_block: str = "latest",
        from_block: int | None = None,
    ) -> JSONLike:
        """Handler method for the 'StakingProcessorUnpaused' events ."""

        instance = cls.get_instance(ledger_api, contract_address)
        to_block = to_block or "latest"
        if to_block == "latest":
            to_block = ledger_api.api.eth.block_number
        from_block = from_block or (to_block - look_back)
        result = instance.events.StakingProcessorUnpaused().get_logs(
            fromBlock=from_block,
            toBlock=to_block,
        )
        return {
            "events": result,
            "from_block": from_block,
            "to_block": to_block,
        }
