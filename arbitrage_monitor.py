import requests
import time

# === Telegram ===
TOKEN = "7695639654:AAHfb52t8d9NwCU33NAgkquqP3mi6tfdg-4"
CHAT_ID = 5732606226

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Ошибка Telegram:", e)

# === Получение цены с бирж ===
def get_binance_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        r = requests.get(url)
        return float(r.json()["price"])
    except:
        return None

def get_bybit_price(symbol):
    try:
        url = f"https://api.bybit.com/v2/public/tickers?symbol={symbol}"
        r = requests.get(url)
        return float(r.json()["result"][0]["last_price"])
    except:
        return None

# === Основная логика ===
def monitor_arbitrage(threshold=3.0):
    pairs = {
        "BTCUSDT": "BTC/USDT",
        "ETHUSDT": "ETH/USDT",
        "SOLUSDT": "SOL/USDT"
    }

    while True:
        for symbol, name in pairs.items():
            binance = get_binance_price(symbol)
            bybit = get_bybit_price(symbol)

            if binance and bybit:
                diff = bybit - binance
                percent = (diff / binance) * 100

                print(f"{name} → Binance: {binance}, Bybit: {bybit}, Δ: {percent:.2f}%")

                if abs(percent) >= threshold:
                    direction = "Bybit дороже" if percent > 0 else "Binance дороже"
                    message = f"💰 Арбитраж: {name}
{direction}
Binance: {binance}
Bybit: {bybit}
Разница: {percent:.2f}%"
                    send_telegram_message(message)
            else:
                print(f"Ошибка получения цены для {name}")

        time.sleep(30)

if __name__ == "__main__":
    print("▶️ Старт арбитражного бота (BTC, ETH, SOL)...")
    monitor_arbitrage()
