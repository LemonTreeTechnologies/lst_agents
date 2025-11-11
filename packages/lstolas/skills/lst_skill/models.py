"""Strategy for the lst agent."""

import re
import html
from typing import Any, cast
from pathlib import Path
from textwrap import dedent
from functools import cached_property
from collections.abc import Callable

from aea.skills.base import Model
from aea.contracts.base import Contract, contract_registry
from aea_ledger_ethereum import Address, EthereumApi, EthereumCrypto
from aea.configurations.base import ContractConfig
from aea.configurations.loader import load_component_configuration
from aea.configurations.data_types import ComponentType

from packages.eightballer.contracts.erc_20 import PUBLIC_ID as ERC20_PUBLIC_ID
from packages.lstolas.contracts.lst_collector import PUBLIC_ID as LST_COLLECTOR_PUBLIC_ID
from packages.eightballer.contracts.amb_gnosis import PUBLIC_ID as AMB_LAYER_2_PUBLIC_ID
from packages.eightballer.contracts.amb_mainnet import PUBLIC_ID as AMB_MAINNET_PUBLIC_ID
from packages.lstolas.contracts.lst_distributor import PUBLIC_ID as LST_DISTRIBUTOR_PUBLIC_ID
from packages.eightballer.contracts.erc_20.contract import Erc20
from packages.lstolas.contracts.lst_activity_module import PUBLIC_ID as LST_ACTIVITY_MODULE_PUBLIC_ID
from packages.lstolas.contracts.lst_staking_manager import PUBLIC_ID as LST_STAKING_MANAGER_PUBLIC_ID
from packages.lstolas.contracts.lst_unstake_relayer import PUBLIC_ID as LST_UNSTAKE_RELAYER_PUBLIC_ID
from packages.lstolas.skills.lst_skill.transactions import signed_tx_to_dict, try_send_signed_transaction
from packages.eightballer.contracts.amb_gnosis_helper import PUBLIC_ID as AMB_GNOSIS_HELPER_PUBLIC_ID
from packages.lstolas.contracts.lst_collector.contract import LstCollector
from packages.eightballer.contracts.amb_gnosis.contract import AmbGnosis as AmbLayer2
from packages.eightballer.contracts.amb_mainnet.contract import AmbMainnet
from packages.lstolas.contracts.lst_distributor.contract import LstDistributor
from packages.lstolas.contracts.lst_staking_processor_l2 import PUBLIC_ID as LST_STAKING_PROCESSOR_L2_PUBLIC_ID
from packages.lstolas.contracts.lst_staking_token_locked import PUBLIC_ID as LST_STAKING_TOKEN_LOCKED_PUBLIC_ID
from packages.eightballer.protocols.user_interaction.message import UserInteractionMessage
from packages.lstolas.contracts.lst_activity_module.contract import LstActivityModule
from packages.lstolas.contracts.lst_staking_manager.contract import LstStakingManager
from packages.lstolas.contracts.lst_unstake_relayer.contract import LstUnstakeRelayer
from packages.eightballer.contracts.amb_gnosis_helper.contract import AmbGnosisHelper
from packages.eightballer.protocols.user_interaction.dialogues import UserInteractionDialogues
from packages.eightballer.connections.apprise_wrapper.connection import CONNECTION_ID as APPRISE_PUBLIC_ID
from packages.lstolas.contracts.lst_staking_processor_l2.contract import LstStakingProcessorL2
from packages.lstolas.contracts.lst_staking_token_locked.contract import LstStakingTokenLocked


ROOT = Path(__file__).parent.parent.parent.parent

GAS_PREMIUM = 1.5  # multiplier to add to the gas price
TX_MINING_TIMEOUT = 300  # seconds
TXN_ATTEMPTS = 3  # number of attempts to send a transaction


def esc_md2(s: str) -> str:
    """Escape to md2."""
    return re.sub(r"([_*\[\]()~`>#+\-=|{}.!])", r"\\\1", s)


def retry_decorator(attempts: int = TXN_ATTEMPTS):
    """Decorator to retry a function call if it returns False."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            def attempt(n):
                result = func(*args, **kwargs)
                if result is not False:
                    return result
                return attempt(n - 1) if n > 1 else False

            return attempt(attempts)

        return wrapper

    return decorator


def load_contract(contract_path: Path) -> Contract:
    """Helper function to load a contract."""
    configuration = cast(ContractConfig, load_component_configuration(ComponentType.CONTRACT, contract_path))
    configuration._directory = contract_path  # noqa
    if str(configuration.public_id) not in contract_registry.specs:
        # load contract into sys modules
        Contract.from_config(configuration)
    return contract_registry.make(str(configuration.public_id))


class LstStrategy(Model):
    """This class implements the strategy of the lst agent."""

    layer_1_api: EthereumApi
    layer_2_api: EthereumApi
    layer_1_starting_block: int
    layer_2_starting_block: int

    # lst contract addresses
    lst_collector_address: Address
    lst_unstake_relayer_address: Address
    lst_distributor_address: Address
    lst_staking_processor_l2_address: Address

    # bridge contract addresses
    layer_2_amb_home: Address
    layer_1_amb_home: Address
    layer_2_amb_helper: Address
    # token contract address
    layer_1_olas_token_address: Address

    # configuration
    bridging_enabled: bool

    def __init__(self, **kwargs):
        """Initialize the strategy of the lst agent."""
        self.layer_1_api = EthereumApi(address=kwargs.pop("layer_1_rpc_endpoint"))
        self.layer_2_api = EthereumApi(address=kwargs.pop("layer_2_rpc_endpoint"))
        self.layer_1_starting_block = kwargs.pop("l1_starting_block")
        self.layer_2_starting_block = kwargs.pop("l2_starting_block")

        self.lst_collector_address = kwargs.pop("lst_collector_address")
        self.lst_unstake_relayer_address = kwargs.pop("lst_unstake_relayer_address")
        self.lst_distributor_address = kwargs.pop("lst_distributor_address")
        self.lst_staking_manager_address = kwargs.pop("lst_staking_manager_address")
        self.lst_staking_processor_l2_address = kwargs.pop("lst_staking_processor_l2_address")

        self.layer_2_amb_home = kwargs.pop("layer_2_amb_home")
        self.layer_1_amb_home = kwargs.pop("layer_1_amb_home")
        self.layer_2_amb_helper = kwargs.pop("layer_2_amb_helper")

        self.layer_1_olas_token_address = kwargs.pop("layer_1_olas_address")
        self.bridging_enabled = kwargs.pop("bridging_enabled", True)

        super().__init__(**kwargs)

    @cached_property
    def lst_collector_contract(self) -> LstCollector:
        """Get the LST Collector contract."""
        return cast(
            LstCollector,
            load_contract(ROOT / LST_COLLECTOR_PUBLIC_ID.author / "contracts" / LST_COLLECTOR_PUBLIC_ID.name),
        )

    @cached_property
    def amb_mainnet_contract(self) -> AmbMainnet:
        """Get the AMB Mainnet contract."""
        return cast(
            AmbMainnet, load_contract(ROOT / AMB_MAINNET_PUBLIC_ID.author / "contracts" / AMB_MAINNET_PUBLIC_ID.name)
        )

    @cached_property
    def layer_2_amb_home_contract(self) -> AmbLayer2:
        """Get the AMB Layer 2 contract."""
        return cast(
            AmbLayer2, load_contract(ROOT / AMB_LAYER_2_PUBLIC_ID.author / "contracts" / AMB_LAYER_2_PUBLIC_ID.name)
        )

    @cached_property
    def layer_2_amb_helper_contract(self) -> AmbGnosisHelper:
        """Get the AMB Gnosis Helper contract."""
        return cast(
            AmbGnosisHelper,
            load_contract(ROOT / AMB_GNOSIS_HELPER_PUBLIC_ID.author / "contracts" / AMB_GNOSIS_HELPER_PUBLIC_ID.name),
        )

    @cached_property
    def lst_unstake_relayer_contract(self) -> LstUnstakeRelayer:
        """Get the LST Unstake Relayer contract."""
        return cast(
            LstUnstakeRelayer,
            load_contract(
                ROOT / LST_UNSTAKE_RELAYER_PUBLIC_ID.author / "contracts" / LST_UNSTAKE_RELAYER_PUBLIC_ID.name
            ),
        )

    @cached_property
    def lst_distributor_contract(self) -> LstDistributor:
        """Get the LST Distributor contract."""
        return cast(
            LstDistributor,
            load_contract(ROOT / LST_DISTRIBUTOR_PUBLIC_ID.author / "contracts" / LST_DISTRIBUTOR_PUBLIC_ID.name),
        )

    @cached_property
    def lst_staking_manager_contract(self) -> LstStakingManager:
        """Get the LST Staking Manager contract."""
        return cast(
            LstStakingManager,
            load_contract(
                ROOT / LST_STAKING_MANAGER_PUBLIC_ID.author / "contracts" / LST_STAKING_MANAGER_PUBLIC_ID.name
            ),
        )

    @cached_property
    def lst_activity_module_contract(self) -> LstActivityModule:
        """Get the LST Activity Module contract."""
        return cast(
            LstActivityModule,
            load_contract(
                ROOT / LST_ACTIVITY_MODULE_PUBLIC_ID.author / "contracts" / LST_ACTIVITY_MODULE_PUBLIC_ID.name
            ),
        )

    @cached_property
    def lst_staking_token_locked(self) -> LstStakingTokenLocked:
        """Get the LST Staking Token Locked contract."""
        return cast(
            LstStakingTokenLocked,
            load_contract(
                ROOT / LST_STAKING_TOKEN_LOCKED_PUBLIC_ID.author / "contracts" / LST_STAKING_TOKEN_LOCKED_PUBLIC_ID.name
            ),
        )

    @cached_property
    def lst_staking_processor_l2_contract(self) -> LstStakingProcessorL2:
        """Get the LST Staking Processor L2 contract."""
        return cast(
            LstStakingProcessorL2,
            load_contract(
                ROOT / LST_STAKING_PROCESSOR_L2_PUBLIC_ID.author / "contracts" / LST_STAKING_PROCESSOR_L2_PUBLIC_ID.name
            ),
        )

    @cached_property
    def layer_1_olas_contract(self) -> Erc20:
        """Get the OLAS token contract."""
        return cast(Erc20, load_contract(ROOT / ERC20_PUBLIC_ID.author / "contracts" / ERC20_PUBLIC_ID.name))

    @cached_property
    def crypto(self) -> EthereumCrypto:
        """Get EthereumCrypto."""
        return EthereumCrypto(private_key_path="ethereum_private_key.txt")

    @property
    def sender_address(self) -> Address:
        """Get the sender address."""
        return cast(Address, self.crypto.address)


class TransactionSettler(Model):
    """Transaction Settler for building transactions."""

    def build_transaction(self, ledger: EthereumApi, func: Any, value: int = 0) -> dict[str, Any] | None:
        """Build the transaction."""

        nonce = ledger._try_get_transaction_count(self.strategy.sender_address)  # noqa: SLF001

        try:
            return func.build_transaction(
                {
                    "from": self.strategy.sender_address,
                    "nonce": nonce,
                    "gas": int(
                        func.estimate_gas({"from": self.strategy.sender_address, "value": value}) * GAS_PREMIUM * 2
                    ),
                    "gasPrice": int(ledger.api.eth.gas_price * GAS_PREMIUM),
                    "value": value,
                }
            )
        except Exception as e:  # pylint: disable=broad-except
            self.log.exception(f"Error building transaction: {e}")
            return None

    def send_notification_to_user(self, msg: str, attach: str | None = None, title: str | None = None) -> None:
        """Send notification to user."""
        dialogues = cast(UserInteractionDialogues, self.context.user_interaction_dialogues)
        msg, _ = dialogues.create(  # type: ignore
            counterparty=str(APPRISE_PUBLIC_ID),
            performative=UserInteractionMessage.Performative.NOTIFICATION,
            title=title,
            body=msg,
            attach=attach,
        )
        self.context.outbox.put_message(message=msg)  # type: ignore

    @retry_decorator(attempts=TXN_ATTEMPTS)
    def build_and_settle_transaction(
        self, contract_address: Address, function: Callable, ledger_api: EthereumApi, **kwargs
    ):
        """Build and settle a transaction."""
        self.log.info(f"Building transaction for contract at address: {contract_address}")
        w3_function = function(
            ledger_api,
            contract_address,
            **kwargs,
        )
        raw_tx = self.build_transaction(
            ledger_api,
            w3_function,
        )
        if raw_tx is None:
            self.log.error("Failed to build transaction.")
            return False

        self.log.info("Signing and sending transaction...")
        signed_tx = signed_tx_to_dict(self.strategy.crypto.entity.sign_transaction(raw_tx))
        tx_hash = try_send_signed_transaction(ledger_api, signed_tx)
        if tx_hash is None:
            self.log.error("Transaction failed after maximum attempts.")
            return False
        self.context.logger.info(f"Transaction hash: {tx_hash.hex()}")
        tx_receipt = ledger_api.api.eth.wait_for_transaction_receipt(tx_hash, timeout=TX_MINING_TIMEOUT)
        if tx_receipt is None or tx_receipt.get("status") != 1:
            self.log.error("Transaction failed...")
            return False
        self.log.info("Transaction successful!")

        chain_id_to_explorer = {
            11155111: "https://sepolia.etherscan.io/tx/",
            10200: "https://gnosis-chiado.blockscout.com/tx/",
            1: "https://etherscan.io/tx/",
            100: "https://gnosisscan.io/tx/",
        }

        args = {str(k): esc_md2(str(v)) for k, v in kwargs.items() if k != "attempts"}
        stringified_args = ", ".join(f"{k}={v}" for k, v in args.items())

        url = chain_id_to_explorer.get(ledger_api.api.eth.chain_id, "") + tx_hash.hex()
        msg = dedent(f"""\
        <b>Function:</b> <code>{html.escape(function.__name__)}</code><br/>
        <b>Contract:</b> <code>{html.escape(contract_address)}</code><br/>
        <b>Kwargs:</b><br/><pre><code>{html.escape(stringified_args)}</code></pre>
        <a href="{html.escape(url)}">Transaction</a>
        Chain ID: {ledger_api.api.eth.chain_id!s}
        """)
        self.log.info(msg)
        self.send_notification_to_user(title="New txn executed!", msg=msg)
        return True

    @property
    def strategy(self) -> LstStrategy:
        """Get the strategy."""
        return cast(LstStrategy, self.context.lst_strategy)

    @property
    def log(self):
        """Get the logger."""
        return self.context.logger

    def simulate(self, contract_address: str, function: Callable, ledger_api: EthereumApi, **kwargs) -> bool:
        """Simulate a transaction."""
        self.log.info(f"Simulating transaction for contract at address: {contract_address}")
        txn = function(
            ledger_api,
            contract_address,
            **kwargs,
        )
        try:
            txn.estimate_gas({"from": self.strategy.sender_address})
            self.log.info("Simulation successful, transaction would be sent.")
            return True
        except Exception as e:  # pylint: disable=broad-except
            self.log.exception(f"Simulation failed, transaction would NOT be sent. Error: {e}")
            return False
