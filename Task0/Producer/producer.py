import sys
import pika

connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbitmq:5672"))
channel = connection.channel()
channel.queue_declare(queue='hello')

print('Producer::Connected to rabbit')

for str in sys.stdin:
    print('Producer::sending_message: ' + str)
    channel.basic_publish(exchange='', routing_key='hello', body=str.encode())

print('Producer::Goodbye!')
