import pika
import time
import psycopg2

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
        time_to_wait *= 2
print('Consumer:: Connected to rabbit')

conn_string = "host='database' dbname='docker_database' user='docker_user'"
time_to_wait = 0.5
while True:
    try:
        dbconn = psycopg2.connect(conn_string)
        break
    except:
        print('Consumer:: unsuccessful connection to database')
        time.sleep(time_to_wait)
        time_to_wait *= 2
print('Consumer:: Connected to database')

dbconn.autocommit = True
cursor = dbconn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, message TEXT NOT NULL);")


def callback(ch, method, properties, body):
    recieved = (body.decode())
    print('Consumer:: Recieved message: ' + recieved)
    print('Consumer:: Putting recieved message into database')
    cursor.execute("INSERT INTO messages VALUES (DEFAULT,%s)", (recieved, ))
    print('Consumer:: Content of database after opperation:')
    cursor.execute("SELECT * FROM messages;")
    for row in cursor:
        print(row)
    
channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()

print('Consumer::Goodbye!')
