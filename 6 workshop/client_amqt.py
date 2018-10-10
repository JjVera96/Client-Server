import pika
import threading
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.60'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

cont = 0

def sent_data():
	sys.stdout.write("Input numbers x, y: ")
	sys.stdout.flush()
	message = sys.stdin.readline()
	if message == '\n':
		print('Good bye')
		sys.exit()
	else:
		message = message.replace('\n', '')
	channel.basic_publish(exchange='', routing_key='+', body=queue_name + ', '+ str(message))
	print(" [x] Sent %r" % message)

def callback(ch, method, properties, body):
	print(" [x] %r" % body)
	sent_data()

sent_data()
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
