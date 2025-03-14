from web3 import Web3

infura_url = "https://www.infura.io/product/ethereum"
web3 = Web3(Web3.HTTPProvider(infura_url))

def check_transaction(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    print(f"🔍 Checking transaction: {tx}")

check_transaction("0x123456...")

