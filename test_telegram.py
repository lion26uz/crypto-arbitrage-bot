import requests

token = "6387414087:AAFAP6KaXq8SzsJJGpEIGnZ2JvqHRNQAkTY"
chat_id = "5980085163"
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
