from brownie import FundMe
from brownie.network.account import Account
from scripts.utils import get_account


def fund(account: Account):
    fund_me = FundMe[-1]

    entrance_fee = fund_me.getEntranceFee()
    print(f"{entrance_fee=}")

    fund_me.fund({"from": account, "value": entrance_fee})
    print("3" * 123)

def withdraw(account: Account):
    fund_me = FundMe[-1]

    fund_me.withdraw({"from": account})


def main():
    account = get_account()

    fund(account)
    withdraw(account)
