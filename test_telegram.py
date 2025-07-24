import requests

# Твой бот-токен и chat_id
token = "6103456789:AAExampleTokenYourBot123456"  # ← сюда подставлен токен
chat_id = "123456789"  # ← сюда подставлен твой chat_id

def send_test_message():
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": "✅ Уведомление работает!"
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Сообщение успешно отправлено.")
    else:
        print("Ошибка отправки:", response.text)

if __name__ == "__main__":
    send_test_message()
