from brownie import SimpleStorage


def main():
    simple_storage = SimpleStorage[-1]

    print(f"{simple_storage.retrieve()=}")
