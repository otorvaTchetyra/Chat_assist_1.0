import datetime
import time

# Время начала и окончания ответа на сообщения
start_time = datetime.time(9, 0)  # 9:00 утра
end_time = datetime.time(18, 0)  # 18:00 вечера

# Функция для проверки времени и ответа на сообщения
def respond_to_messages():
    now = datetime.datetime.now().time()
    if start_time <= now <= end_time:
        print("Ответ на сообщения включен.")
    else:
        print("Ответ на сообщения выключен.")

# Основной цикл
while True:
    respond_to_messages()
    time.sleep(10)  # Ждем 10 секунду перед следующим вызовом