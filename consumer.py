import json
import os
import sys

import pika


def callback(ch, method, properties, body):
    detection = json.loads(body)
    license_plate = detection['license_plate']
    print("Received license_plate:", license_plate)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='detections')
channel.basic_consume(queue='detections', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

channel.close()
connection.close()
