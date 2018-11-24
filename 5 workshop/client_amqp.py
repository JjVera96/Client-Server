import pika
import threading
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.60'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

def send_data():
	sys.stdout.write("Input numbers x, y: ")
	sys.stdout.flush()
	message = sys.stdin.readline()
	if message == '\n':
		print('Good bye')
		connection.close()
		sys.exit()
	else:
		message = message.replace('\n', '')
		print(message)
	channel.basic_publish(exchange='', routing_key='+', body=queue_name + ', '+ str(message))
	print(" [x] Sent %r" % message)

def callback(ch, method, properties, body):
	print(" [x] %r" % body)
	send_data()

send_data()
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()
