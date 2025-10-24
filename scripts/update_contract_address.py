"""Update the default contracts address in configurations skill."""

import re
import json
from pathlib import Path

from aea.configurations.base import PublicId, ComponentId, ComponentType


LST_COMPONENT_ID = ComponentId(ComponentType.SKILL, PublicId.from_str("lstolas/lst_skill:0.1.0"))

CONTRACT_DEPLOYMENT_PATH = (
    Path(__file__).parent.parent.parent / "olas-lst" / "scripts" / "deployment" / "globals_gnosis_chiado.json"
)


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
    def load_config_file(cls) -> dict:
        """Load the configuration file."""
        with open(CONTRACT_DEPLOYMENT_PATH, encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def load_required_contracts(cls) -> dict:
        """Load the required contracts from the configuration file."""
        config_data = cls.load_config_file()
        return {
            config_key: config_data[contract_key] for config_key, contract_key in ConfigKeyToContractKey.mapping.items()
        }

    @staticmethod
    def update_contracts_in_skill(new_contracts: dict):
        """Update the contracts in the skill configuration file."""
        skill_config_path = (
            Path(__file__).parent.parent
            / "packages"
            / LST_COMPONENT_ID.public_id.author
            / (LST_COMPONENT_ID.component_type.value + "s")
            / LST_COMPONENT_ID.public_id.name
            / "skill.yaml"
        )
        if not skill_config_path.exists():
            msg = f"Skill configuration file not found at {skill_config_path}"
            raise FileNotFoundError(msg)

        with open(skill_config_path, encoding="utf-8") as f:
            skill_config = f.read()

        for config_key, new_address in new_contracts.items():
            pattern = rf"(?m)^(?P<indent>\s*){re.escape(config_key)}:\s*['\"]?.*?['\"]?\s*$"
            replacement = rf"\g<indent>{config_key}: '{new_address}'"
            skill_config = re.sub(pattern, replacement, skill_config)

        with open(skill_config_path, "w", encoding="utf-8") as f:
            f.write(skill_config)

    @classmethod
    def process(cls):
        """Update the default contracts address in configurations skill."""

        new_contracts = cls.load_required_contracts()
        cls.update_contracts_in_skill(new_contracts)


if __name__ == "__main__":
    ConfigKeyToContractKey.process()
