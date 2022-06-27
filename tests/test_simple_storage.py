from brownie import SimpleStorage

from scripts.utils import deploy_contract


def test_deploy(accounts):
    simple_storage = deploy_contract(
        contract=SimpleStorage,
        account=accounts[0],
        force=True
    )

    assert simple_storage.retrieve() == 0


def test_updating_storage(accounts):
    account = accounts[0]
    new_value = 15

    simple_storage = deploy_contract(
        contract=SimpleStorage,
        account=account,
        force=True
    )
    simple_storage.store(new_value, {"from": account})

    assert simple_storage.retrieve() == new_value
