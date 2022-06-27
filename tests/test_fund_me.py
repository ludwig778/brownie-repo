from pytest import raises

from brownie.exceptions import VirtualMachineError

from scripts.fund_me.deploy import deploy_fund_me


def test_can_fund_and_withdraw(accounts):
    account = accounts[0]

    fund_me = deploy_fund_me(account, force=True)

    entrance_fee = fund_me.getEntranceFee() + 100

    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx = fund_me.withdraw({"from": account})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw(accounts):
    fund_me = deploy_fund_me(accounts[0], force=True)

    with raises((VirtualMachineError, ValueError), match="Owner needed!"):
        fund_me.withdraw({"from": accounts[1]})
