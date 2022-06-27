from brownie import SimpleStorage
from brownie.network.account import Account

from scripts.utils import get_account, deploy_contract


def deploy_simple_storage(account: Account):
    return deploy_contract(SimpleStorage, account, force=True)

def main():
    account = get_account()

    deploy_simple_storage(account)
