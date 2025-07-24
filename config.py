from parser import parse_binance, parse_bybit, parse_okx, parse_bestchange

settings = {
    "check_interval": 60,  # интервал в секундах между проверками

    "min_profit_percent": 3,  # минимальный процент прибыли для уведомления

    "pairs": [
        ["USDC", "PLN"],
        ["BTC", "USDC"],
        ["ETH", "USDC"],
        ["SOL", "USDC"],
        ["USDT", "PLN"],
        ["USDT", "BTC"],
        ["USDT", "ETH"],
        ["USDT", "SOL"],
        ["BTC", "ETH"],
        ["BTC", "SOL"],
        ["ETH", "SOL"]
    ],

    "exchanges": {
        "binance": {
            "parser": parse_binance
        },
        "bybit": {
            "parser": parse_bybit
        },
        "okx": {
            "parser": parse_okx
        },
        "bestchange": {
            "parser": parse_bestchange
        }
    },

    "telegram": {
        "token": "вставь_сюда_свой_token",
        "chat_id": 123456789
    }
}
