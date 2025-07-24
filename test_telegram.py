import requests

# 🔐 Данные для Telegram
token = "6387414087:AAFAP6KaXq8SzsJJGpEIGnZ2JvqHRNQAkTY"
chat_id = 5685233203

# 📩 Текст уведомления
message = """
✅ Уведомление из арбитражного бота
Бот успешно отправил сообщение в Telegram.
Все работает корректно.
"""

# 📤 Отправка сообщения
url = f"https://api.telegram.org/bot{token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(url, data=payload)

# 📋 Вывод результата
print("Статус отправки:", response.status_code)
print("Ответ сервера:", response.text)
