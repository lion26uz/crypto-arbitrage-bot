settings = {
    "exchanges": {
        "bybit": {
            "url": "https://api.bybit.com/v2/public/tickers?symbol={pair}",
            "parser": lambda response: float(response.json()["result"][0]["last_price"]),
            "pairs": ["BTCUSDT", "ETHUSDT", "SOLUSDT", "USDCPLN", "USDTPLN"]
        },
        "okx": {
            "url": "https://www.okx.com/api/v5/market/ticker?instId={pair}",
            "parser": lambda response: float(response.json()["data"][0]["last"]),
            "pairs": ["BTC-USDT", "ETH-USDT", "SOL-USDT", "USDC-PLN", "USDT-PLN"]
        },
        "binance": {
            "url": "https://api.binance.com/api/v3/ticker/price?symbol={pair}",
            "parser": lambda response: float(response.json()["price"]),
            "pairs": ["BTCUSDT", "ETHUSDT", "SOLUSDT", "USDCPLN", "USDTPLN"]
        }
    },
    "check_interval": 60,  # интервал в секундах
    "min_profit_percent": 3.0,  # минимальный процент прибыли
    "telegram": {
        "token": "вставь_сюда_свой_token",  # вставь сюда свой токен
        "chat_id": 123456789               # вставь сюда свой chat_id
    }
}
