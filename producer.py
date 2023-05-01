import json

import pika, os, logging, time

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='detections')

with open(r'сar_data.json', mode='r', encoding='utf-8') as f:
    detections = json.load(f)

for detection_key in detections.keys():
    message = json.dumps(detections[detection_key], ensure_ascii=False)
    channel.basic_publish(exchange='', routing_key='detections', body=message)
    print("Sent message:", message)
    time.sleep(2)

channel.close()
connection.close()
