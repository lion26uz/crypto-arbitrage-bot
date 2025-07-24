import requests
from config import settings

def send_telegram_message(message):
    token = settings["telegram"]["token"]
    chat_id = settings["telegram"]["chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Ошибка Telegram: {e}")
