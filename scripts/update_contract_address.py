"""Update the default contracts address in configurations skill."""

import re
import json
from pathlib import Path

from aea.configurations.base import PublicId, ComponentId, ComponentType
from enum import Enum


LST_COMPONENT_ID = ComponentId(ComponentType.SKILL, PublicId.from_str("lstolas/lst_skill:0.1.0"))
PROD_AGENT_ID = PublicId.from_str("lstolas/lst_agent_prod:0.1.0")

TESTNET_CONTRACT_DEPLOYMENT_PATH = (
    Path(__file__).parent.parent.parent / "olas-lst" / "scripts" / "deployment" / "globals_gnosis_chiado.json"
)

PRODUCTION_CONTRACT_DEPLOYMENT_PATH_L1 = (
    Path(__file__).parent.parent.parent / "olas-lst" / "scripts" / "deployment" / "globals_eth_mainnet.json"
)
PRODUCTION_CONTRACT_DEPLOYMENT_PATH_L2 = (
    Path(__file__).parent.parent.parent / "olas-lst" / "scripts" / "deployment" / "globals_gnosis_mainnet.json"
)

class DeploymentType(Enum):
    """Enum for deployment types."""

    TESTNET = "testnet"
    PRODUCTION = "production"


    @property
    def contract_deployment_paths(self) -> Path:
        """Get the contract deployment path based on deployment type."""
        if self == DeploymentType.TESTNET:
            return [TESTNET_CONTRACT_DEPLOYMENT_PATH]
        elif self == DeploymentType.PRODUCTION:
            return [
                PRODUCTION_CONTRACT_DEPLOYMENT_PATH_L1,
                PRODUCTION_CONTRACT_DEPLOYMENT_PATH_L2,
            ]
        else:
            raise ValueError(f"Unsupported deployment type: {self.value}")

    @property
    def component_path(self) -> Path:
        """Get the component path based on deployment type."""
        if self == DeploymentType.TESTNET:
            return (
                Path(__file__).parent.parent
                / "packages"
                / LST_COMPONENT_ID.public_id.author
                / (LST_COMPONENT_ID.component_type.value + "s")
                / LST_COMPONENT_ID.public_id.name
                / "skill.yaml"
            )
        elif self == DeploymentType.PRODUCTION:
            return (
                Path(__file__).parent.parent
                / "packages"
                / PROD_AGENT_ID.author
                / "agents"
                / PROD_AGENT_ID.name
                / "aea-config.yaml"
            )

        else:
            raise ValueError(f"Unsupported deployment type: {self.value}")


KEYS_TO_SKIP = [
    "providerName",
    "chainId",
    "networkURL",
    "blockscoutURL",
    "olasAddress",
    "gnosisOmniBridgeAddress"
]

class ConfigKeyToContractKey:
    """Enum for mapping configuration keys to contract keys."""

    mapping: dict = {
        "lst_collector_address": "collectorProxyAddress",
        "lst_unstake_relayer_address": "unstakeRelayerProxyAddress",
        "lst_distributor_address": "distributorProxyAddress",
        "lst_staking_manager_address": "stakingManagerProxyAddress",
        "lst_staking_processor_l2_address": "gnosisStakingProcessorL2Address",
    }

    @classmethod
    def load_config_file(cls, deployment_type: DeploymentType) -> dict:
        """Load the configuration file."""
        
        data = {}
        for deployment_path in deployment_type.contract_deployment_paths:
            if not deployment_path.exists():
                msg = f"Contract deployment file not found at {deployment_path}"
                raise FileNotFoundError(msg)
        
            new_data = json.loads(Path(deployment_path).read_text(encoding="utf-8"))
            for key, value in new_data.items():
                if key in KEYS_TO_SKIP:
                    continue
                if key in data:
                    old_value = data[key]
                    if old_value != value:
                        msg = f"Conflict for key {key}: {old_value} != {value}"
                        raise ValueError(msg)
                data[key] = value
        return data



    @classmethod
    def load_required_contracts(cls, deployment_type: DeploymentType) -> dict:
        """Load the required contracts from the configuration file."""
        config_data = cls.load_config_file(deployment_type)
        return {
            config_key: config_data[contract_key] for config_key, contract_key in ConfigKeyToContractKey.mapping.items()
        }

    @staticmethod
    def update_contracts_in_config(new_contracts: dict, deployment_type: DeploymentType) -> None:
        """Update the contracts in the skill configuration file."""
        config_path = deployment_type.component_path
        if not config_path.exists():
            msg = f"configuration file not found at {config_path}"
            raise FileNotFoundError(msg)

        config = Path(config_path).read_text(encoding="utf-8")

        for config_key, new_address in new_contracts.items():
            pattern = rf"(?m)^(?P<indent>\s*){re.escape(config_key)}:\s*['\"]?.*?['\"]?\s*$"
            replacement = rf"\g<indent>{config_key}: '{new_address}'"
            config = re.sub(pattern, replacement, config)
        Path(config_path).write_text(config, encoding="utf-8")


    @classmethod
    def process(cls):
        """Update the default contracts address in configurations skill."""

        for deployment_type in DeploymentType:
            print(f"Updating contracts for deployment type: {deployment_type.value}")
            new_contracts = cls.load_required_contracts(deployment_type)
            cls.update_contracts_in_config(new_contracts, deployment_type)


if __name__ == "__main__":
    ConfigKeyToContractKey.process()
