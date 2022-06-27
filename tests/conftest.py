from pytest import fixture

from brownie import network

from scripts.constants import FORKED_ENVS, LOCAL_ENVS


@fixture(scope="session", autouse=True)
def ensure_dev_env_is_used():
    if network.show_active() not in LOCAL_ENVS + FORKED_ENVS:
        raise Exception("Tests can be runned only in dev environments")
