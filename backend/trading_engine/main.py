import requests
import numpy as np

API_URL = "https://api.binance.com/api/v3/ticker/price"

def price(symbol):
    response = requests.get(f"{API_URL}?symbol={symbol}")
    return float(response.json()["price"])

def strategy():
    btc_price = price("BTCUSDT")
    eth_price = price("ETHUSDT")

    if btc_price > eth_price * 14:
        print("📈 Buy ETH, Sell BTC")
    else:
        print("📉 Buy BTC, Sell ETH")

if __name__ == "__main__":
    strategy()
