#!/usr/bin/env bash
set -eu

function generate_contracts() {
    local abi_path=$1
    local contract_name=$2
    local contract_author=lstolas

    echo removing old contract at packages/${contract_author}/contracts/${contract_name}
    rm -rf packages/${contract_author}/contracts/${contract_name}
    adev scaffold contract --from-abi "$abi_path" "${contract_author}/${contract_name}"
}

generate_contracts ../olas-lst/abis/0.8.30/StakingTokenLocked.json lst_staking_token_locked
generate_contracts ../olas-lst/abis/0.8.30/Collector.json lst_collector
generate_contracts ../olas-lst/abis/0.8.30/ActivityModule.json lst_activity_module
generate_contracts ../olas-lst/abis/0.8.30/Distributor.json lst_distributor
generate_contracts ../olas-lst/abis/0.8.30/UnstakeRelayer.json lst_unstake_relayer
generate_contracts ../olas-lst/abis/0.8.30/GnosisStakingProcessorL2.json lst_staking_processor_l2
generate_contracts ../olas-lst/abis/0.8.30/StakingManager.json lst_staking_manager
