import json
import os
import sys

import pika

from Project_Practice.create_picture import create_detection_image

'''Функция callback вызывается каждый раз, когда в очереди detections появляется новое сообщение'''


def callback(ch, method, properties, body):
    detection = json.loads(body)
    license_plate = detection['license_plate']
    print("Received license_plate:", license_plate)
    create_detection_image(detection)


''' устанавливается соединение с локальным экземпляром RabbitMQ, 
создается канал, на котором объявляется очередь detections.
Функция start_consuming() начинает получение сообщений из очереди и переводит канал в режим потребления сообщений.'''

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='detections')
channel.basic_consume(queue='detections', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

# закрытие соединения
channel.close()
connection.close()
