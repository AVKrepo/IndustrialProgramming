import sys
import pika
import time

time_to_wait = 0.5
while True:
    try:
        connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbitmq:5672"))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        break
    except:
        print('Consumer:: unsuccessful connection to rabbit')
        time.sleep(time_to_wait)
        time_to_wait = time_to_wait * 2

print('Consumer:: Connected to rabbit')

def callback(ch, method, properties, body):
    recieved = (body.decode())
    print('Consumer:: Recieved message: ' + recieved)
    
channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()

print('Consumer::Goodbye!')
