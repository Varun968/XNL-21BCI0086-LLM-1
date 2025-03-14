from fastapi import FastAPI, HTTPException
import uvicorn
import redis
import json
import time
import websockets
import asyncio
import numpy as np

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
MARKET_DATA_WS = "wss://stream.binance.com:9443/ws/btcusdt@trade"
active_orders = {}

def ai_trade_decision(price):
    if np.random.rand() > 0.5:
        return "BUY"
    else:
        return "SELL"

def execute_trade(order_id, asset, quantity, price, trade_type):
    execution_time = time.time()
    ai_decision = ai_trade_decision(price)
    
    if trade_type != ai_decision:
        return {"status": "rejected", "reason": "AI Risk Model Rejection"}

    trade_data = {
        "order_id": order_id,
        "asset": asset,
        "quantity": quantity,
        "price": price,
        "trade_type": trade_type,
        "execution_time": execution_time
    }
    redis_client.set(order_id, json.dumps(trade_data))

    return {"status": "executed", "trade_data": trade_data}

@app.post("/trade")
async def trade(asset: str, quantity: float, price: float, trade_type: str):
    if trade_type not in ["BUY", "SELL"]:
        raise HTTPException(status_code=400, detail="Invalid trade type")

    order_id = f"order_{int(time.time() * 1000)}"
    result = execute_trade(order_id, asset, quantity, price, trade_type)
    return result

async def market_data_listener():
    async with websockets.connect(MARKET_DATA_WS) as ws:
        while True:
            data = await ws.recv()
            trade_data = json.loads(data)
            price = float(trade_data["p"])
            print(f"Real-Time Price: {price}")  

@app.on_event("startup")
async def start_market_data_listener():
    asyncio.create_task(market_data_listener())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
