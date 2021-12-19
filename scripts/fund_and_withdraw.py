from brownie import FundMe
from scripts.util import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()

    entrance_fee = fund_me.getEntranceFee()
    print("Current entrance fee is", entrance_fee)
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()

    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
