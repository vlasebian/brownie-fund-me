from brownie import accounts, config, network
from brownie import MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000 * (10 ** 8)

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def deploy_mocks():
    print("The active network is", network.show_active())
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            # Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account()},
        )
    print("Mocks deployed.")


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
