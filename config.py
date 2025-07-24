exchanges = {
    "bybit": {
        "url": "https://api.bybit.com/v2/public/tickers?symbol={pair}",
        "parser": lambda response: float(response.json()["result"][0]["last_price"])
    },
    "binance": {
        "url": "https://api.binance.com/api/v3/ticker/price?symbol={pair}",
        "parser": lambda response: float(response.json()["price"])
    },
    "okx": {
        "url": "https://www.okx.com/api/v5/market/ticker?instId={pair}",
        "parser": lambda response: float(response.json()["data"][0]["last"])
    }
}

pairs = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "USDCUSDT",
    "USDTPLN",
    "USDCEUR"
]

threshold = 3.0  # минимальный % прибыли для уведомлений

TELEGRAM_TOKEN = "вставь_сюда_токен_бота"
CHAT_ID = 5732066226  # твой Telegram ID
