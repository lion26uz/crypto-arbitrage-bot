import time
from notifier import send_telegram_message
from config import settings
from exchanges import fetch_price

pairs_to_check = [
    ("BTC/USDC", ["binance", "bybit", "okx"]),
    ("ETH/USDC", ["binance", "bybit", "okx"]),
    ("SOL/USDC", ["binance", "bybit", "okx"]),
    ("USDC/PLN", ["binance", "bybit", "okx"]),
]

def check_arbitrage(pair):
    base, quote = pair.split('/')
    prices = {}

    for exchange in settings["exchanges"]:
        if pair in settings["exchanges"][exchange]["symbols"]:
            try:
                price = fetch_price(exchange, pair)
                if price:
                    prices[exchange] = price
            except Exception as e:
                print(f"Ошибка при получении цены с {exchange}: {e}")

    if len(prices) < 2:
        return

    min_exchange = min(prices, key=prices.get)
    max_exchange = max(prices, key=prices.get)

    buy_price = prices[min_exchange]
    sell_price = prices[max_exchange]
    profit_percent = ((sell_price - buy_price) / buy_price) * 100

    if profit_percent >= settings["min_profit_percent"]:
        message = (
            f"🔁 Арбитраж обнаружен:\n"
            f"{pair}\n"
            f"Купить на {min_exchange}: {buy_price:.2f}\n"
            f"Продать на {max_exchange}: {sell_price:.2f}\n"
            f"📈 Профит: {profit_percent:.2f}%"
        )
        print(message)
        send_telegram_message(message)

if __name__ == "__main__":
    print("Бот запущен.")
    while True:
        for pair, exchanges in pairs_to_check:
            check_arbitrage(pair)
        time.sleep(settings["check_interval_seconds"])
