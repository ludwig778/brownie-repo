from typing import Any, List, Optional

from brownie import accounts, config, network, Contract
from brownie.network.account import Account

from scripts.constants import FORKED_ENVS, LOCAL_ENVS


def get_account():
    current_network = network.show_active()
    if current_network in LOCAL_ENVS + FORKED_ENVS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_contract(
    contract: Contract,
    account: Account,
    args: Optional[List[Any]] = None,
    verify: bool = False,
    force: bool = False,
):
    if len(contract) > 0 and not force:
        return contract[-1]

    if not args:
        args = []

    return contract.deploy(*args, {"from": account}, publish_source=verify)
