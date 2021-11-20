from brownie import (
    accounts,
    MockV3Aggregator,
    network,
)

DECIMALS = 8
# This is 4,400
INITIAL_VALUE = 440000000000


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet/local
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = accounts[0]
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")


def main():
    deploy_mocks()
