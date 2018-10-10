#!/usr/bin/env python
import pika
import re

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.60'))
channel = connection.channel()
channel.queue_declare(queue='+')

pattern = re.compile("[\w._-]+, [\d]+, [\d]+")

def callback(ch, method, properties, body):
	print(" [x] %r" % body)
	data = body.decode()
	print(data)
	if pattern.match(data):
		queue_name, op1, op2 = data.split(', ')
		result = str(int(op1) + int(op2))
	else:
		queue_name, other = data.split(', ', 1)
		result = 'Match Error. Struct for operation queue_name, op, op with spaces.'		
	print(result)
	try:
		channel.basic_publish(exchange='', routing_key=queue_name, body=result)
	except:
		print('Error in comunication.')

channel.basic_consume(callback, queue='+',  no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
