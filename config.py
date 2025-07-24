settings = {
    "telegram": {
        "token": "вставь_сюда_свой_token",
        "chat_id": 123456789
    },
    "min_profit_percent": 3.0,
    "check_interval_seconds": 60,
    "exchanges": {
        "binance": {
            "symbols": ["BTC/USDC", "ETH/USDC", "SOL/USDC", "USDC/PLN"],
            "url": "https://api.binance.com/api/v3/ticker/price?symbol={}",
            "parser": lambda r: float(r.json()["price"])
        },
        "bybit": {
            "symbols": ["BTC/USDC", "ETH/USDC", "SOL/USDC", "USDC/PLN"],
            "url": "https://api.bybit.com/v2/public/tickers?symbol={}",
            "parser": lambda r: float(r.json()["result"][0]["last_price"])
        },
        "okx": {
            "symbols": ["BTC/USDC", "ETH/USDC", "SOL/USDC", "USDC/PLN"],
            "url": "https://www.okx.com/api/v5/market/ticker?instId={}",
            "parser": lambda r: float(r.json()["data"][0]["last"])
        }
    }
}
