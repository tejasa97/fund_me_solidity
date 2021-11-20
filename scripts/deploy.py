from brownie import accounts, config, FundMe, MockV3Aggregator
from scripts.helpful_scripts import deploy_mocks

def deploy():

    deploy_mocks()
    account = accounts[0]
    price_feed_address = MockV3Aggregator[-1].address
    fund_me_contract = FundMe.deploy(price_feed_address, {"from": account})
    

def main():
    deploy()