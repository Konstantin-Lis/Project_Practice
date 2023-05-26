import json
import time

import pika
from Project_Practice.main import check, new_car, new_data, whole_data, deside, REAL_TIME, fixate_violation
global whole_data

'''Функция callback вызывается каждый раз, когда в очереди detections появляется новое сообщение'''


def callback(ch, method, properties, body):
    detection = json.loads(body)
    license_plate = detection['license_plate']
    print("Получены данные по номеру:", license_plate)
    if check(detection) == -1:
        new_car(detection)
    new_data(detection)



''' устанавливается соединение с локальным экземпляром RabbitMQ, 
создается канал, на котором объявляется очередь detections.
Функция start_consuming() начинает получение сообщений из очереди и переводит канал в режим потребления сообщений.'''

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='detections')
channel.basic_consume(queue='detections', on_message_callback=callback, auto_ack=True)

print('Ожидание новых сообщений...')

for dct in whole_data:
    if deside(dct["LIGHTS"]) == 1:
        fixate_violation(dct)

channel.start_consuming()

# закрытие соединения
channel.close()
connection.close()





