from brownie import MockV3Aggregator, FundMe, config, network
from brownie.network.account import Account

from scripts.utils import get_account, deploy_contract
from scripts.constants import DECIMALS, STARTING_PRICE, LOCAL_ENVS


def deploy_fund_me(account: Account, force: bool = False):
    current_network = network.show_active()
    current_network_config = config["networks"][current_network]

    if not (price_feed_address := current_network_config.get("eth_usd_price_feed")):
        mock_aggregator = deploy_contract(
            contract=MockV3Aggregator,
            account=account,
            args=[DECIMALS, STARTING_PRICE],
            force=force
        )
    
        price_feed_address = mock_aggregator.address

    return deploy_contract(
        contract=FundMe,
        account=account,
        args=[price_feed_address],
        verify=current_network_config.get("verify", False),
        force=force
    )


def main():
    account = get_account()

    deploy_fund_me(account)
