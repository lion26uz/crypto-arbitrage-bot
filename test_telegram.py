import requests

token = "6103456789:AAExampleTokenYourBot123456"  # сюда твой токен
chat_id = "123456789"  # сюда твой chat_id

message = "✅ Telegram уведомление работает!"

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Сообщение отправлено в Telegram!")
else:
    print("Ошибка:", response.text)
