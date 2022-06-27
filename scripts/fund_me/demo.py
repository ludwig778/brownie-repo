from scripts.fund_me.deploy import deploy_fund_me
from scripts.utils import get_account


def main():
    account = get_account()

    fund_me = deploy_fund_me(account=account, force=True)
    
    print(f"{fund_me.getConversionRate(1e18) / 1e18=}")

    entrance_fee = fund_me.getEntranceFee()
    print(f"{fund_me.getConversionRate(entrance_fee) / 1e18=}")
