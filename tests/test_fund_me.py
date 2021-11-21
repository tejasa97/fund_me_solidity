from brownie import network, FundMe
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def test_can_fund_and_withdraw():

    print(network.show_active())
    fund_me_contract = deploy_fund_me()

    account = get_account()
    entrance_fee = fund_me_contract.getEntranceFee() + 2

    tx = fund_me_contract.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fund_me_contract.addressToAmountFunded(account.address) == entrance_fee
