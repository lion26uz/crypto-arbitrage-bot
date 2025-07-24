
import requests

TOKEN = '7695639654:AAHfb52t8d9NwCU33NAgkquqP3mi6tfdg-4'
CHAT_ID = '5732606226'

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Ошибка отправки уведомления: {e}")
