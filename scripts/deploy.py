from brownie import accounts, config, FundMe, MockV3Aggregator, network
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    deploy_mocks,
    get_account,
)


def deploy_fund_me():
    """Deploys the contract to Local/Testnet"""

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        deploy_mocks()
        price_feed_contract_address = MockV3Aggregator[-1].address
    else:
        price_feed_contract_address = config["networks"][network.show_active()][
            "eth_usd_price_contract"
        ]

    account = get_account()
    fund_me_contract = FundMe.deploy(price_feed_contract_address, {"from": account})

    print(f"Contract deployed to {fund_me_contract.address}")
    return fund_me_contract


def main():
    deploy_fund_me()
