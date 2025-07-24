def parse_binance(data):
    return float(data["price"])

def parse_bybit(data):
    return float(data["result"][0]["price"]) if "result" in data and data["result"] else None

def parse_okx(data):
    return float(data["data"][0]["last"])

settings = {
    "pairs": ["BTC-USDT", "ETH-USDT", "SOL-USDT"],
    "check_interval": 20,  # в секундах
    "min_profit_percent": 3.0,  # минимальный процент прибыли

    "exchanges": {
        "binance": {
            "url": "https://api.binance.com/api/v3/ticker/price?symbol={pair}",
            "parser": parse_binance
        },
        "bybit": {
            "url": "https://api.bybit.com/v5/market/tickers?category=spot&symbol={pair}",
            "parser": parse_bybit
        },
        "okx": {
            "url": "https://www.okx.com/api/v5/market/ticker?instId={pair}",
            "parser": parse_okx
        }
    }
}
