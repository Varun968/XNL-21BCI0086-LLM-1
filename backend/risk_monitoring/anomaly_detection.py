from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:3000")

def log_trade(symbol, price, volume, risk_level):
    doc = {
        "symbol": symbol,
        "price": price,
        "volume": volume,
        "risk": risk_level
    }
    es.index(index="trade_logs", body=doc)

log_trade("BTCUSD", 42000, 500, "Low")