settings = {
    "telegram": {
        "token": "bot_saryuch",   # заменено на твой токен
        "chat_id": 123456789      # заменено на твой chat_id
    },
    "check_interval": 60,
    "exchanges": {
        "bybit": {
            "url": "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT",
            "parser": lambda r: float(r.json()["result"][0]["last_price"])
        },
        "binance": {
            "url": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
            "parser": lambda r: float(r.json()["price"])
        }
    },
    "pairs": [
        ["bybit", "binance", "BTCUSDT"],
        ["binance", "bybit", "BTCUSDT"]
    ],
    "min_profit_percent": 1.5
}
