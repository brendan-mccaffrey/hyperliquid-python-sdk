import example_utils

from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants


def main():
    address, info, exchange = example_utils.setup(constants.TESTNET_API_URL, skip_ws=True)

    # Change this address to a vault that you want to deposit/withdraw
    vault_address = "0xa15099a30bbf2e68942d6f4c43d70d04faeab0a0"
    is_deposit = True
    usd_amount = 5

    # Deposit $5 into a vault
    transfer_result = exchange.vault_transfer(vault_address, is_deposit, usd_amount)
    print(transfer_result)


if __name__ == "__main__":
    main()
