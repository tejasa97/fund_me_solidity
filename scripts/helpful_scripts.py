from brownie import accounts, MockV3Aggregator, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development"]

DECIMALS = 8
INITIAL_VALUE = 440000000000  # This is 4,400 (approx current price of Ethereum)


def get_account():
    """Returns the wallet account to use"""

    # If local dev network
    if network.show_active() in [LOCAL_BLOCKCHAIN_ENVIRONMENTS]:
        return accounts[0]

    # If live network
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    """Use this script if you want to deploy mocks to a Local network
    Testnets like Rinkeby, Kovan usually have the ChainLink Pricefeed contract deployed on them
    """

    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = accounts[0]
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")
