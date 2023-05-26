import json

import pika, os, logging, time

'''создание подключения к RabbitMQ, создание соединения и канала, и определяется очередь 'detections'.'''
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='detections')

'''Открытие файла car_data.json и загрузка содержимого в переменную detections с помощью модуля json.'''
with open('сar_data.json', mode='r', encoding='utf-8') as f:
    for line in f:
        detection = json.loads(line)
        message = json.dumps(detection, ensure_ascii=False)
        channel.basic_publish(exchange='', routing_key='detections', body=message)
        print("Сообщение отправлено:", message)
        time.sleep(1)

'''перебор всех ключей в словаре detections и отправка каждого значения в очередь detections. 
Затем выводится сообщение о том, что сообщение было отправлено'''



# закрытие соединения
channel.close()
connection.close()
