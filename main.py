import time
import requests
from config import settings

def fetch_price(exchange, pair):
    url = settings["exchanges"][exchange]["url"].format(pair=pair)
    response = requests.get(url)
    if response.status_code == 200:
        return settings["exchanges"][exchange]["parser"](response.json())
    return None

def check_arbitrage(pair):
    prices = {}
    for exchange in settings["exchanges"]:
        price = fetch_price(exchange, pair)
        if price:
            prices[exchange] = price

    if len(prices) < 2:
        return

    sorted_prices = sorted(prices.items(), key=lambda x: x[1])
    buy_exchange, buy_price = sorted_prices[0]
    sell_exchange, sell_price = sorted_prices[-1]
    profit = ((sell_price - buy_price) / buy_price) * 100

    if profit >= settings["min_profit_percent"]:
        print(f"[!] Арбитраж: купить на {buy_exchange} за {buy_price}, продать на {sell_exchange} за {sell_price} → Профит: {profit:.2f}%")

if __name__ == "__main__":
    print("Бот запущен.")
    while True:
        for pair in settings["pairs"]:
            check_arbitrage(pair)
        time.sleep(settings["check_interval"])
