"""Simple script to read in and update the contract addresses from the config file."""

import re
import json
from pathlib import Path


AGENT_CONFIG_PATH = (
    Path(__file__).parent.parent / "packages" / "lstolas" / "agents" / "lst_agent_prod" / "aea-config.yaml"
)
DEPLOYMENT_CONFIG = Path(__file__).parent.parent.parent / "olas-lst" / "doc" / "configuration.json"


mainnet_mapping: dict = {
    "lst_unstake_relayer_address": "UnstakeRelayerProxy",
    "lst_distributor_address": "DistributorProxy",
}


gnosis_mapping: dict = {
    "lst_staking_processor_l2_address": "GnosisStakingProcessorL2",
    "lst_collector_address": "CollectorProxy",
    "lst_staking_manager_address": "StakingManagerProxy",
}


def do_update():
    """Update the contract addresses in the agent configuration file."""
    config_vars = json.loads(DEPLOYMENT_CONFIG.read_text(encoding="utf-8"))

    mainnet_config = config_vars[0]
    layer2_config = config_vars[1]

    for mapping, config in [(mainnet_mapping, mainnet_config), (gnosis_mapping, layer2_config)]:

        for config_key, contract_key in mapping.items():
            found = False
            for item in config["contracts"]:
                if item["name"] == contract_key:
                    new_address = item["address"]
                    update_config_file(config_key, new_address)
                    found = True
            if not found:
                pass


def update_config_file(config_key: str, new_address: str) -> str:
    """Update the configuration file with the new contract address."""

    agent_config_text = AGENT_CONFIG_PATH.read_text(encoding="utf-8")
    pattern = rf"(?m)^(?P<indent>\s*){re.escape(config_key)}:\s*['\"]?.*?['\"]?\s*$"
    replacement = rf"\g<indent>{config_key}: '{new_address}'"
    updated_text = re.sub(pattern, replacement, agent_config_text)
    AGENT_CONFIG_PATH.write_text(updated_text, encoding="utf-8")


if __name__ == "__main__":
    do_update()
