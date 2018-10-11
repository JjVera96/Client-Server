#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.60'))
channel = connection.channel()
channel.queue_declare(queue='+')
pattern = re.compile("[\d]+, [\d]+")

def sum(data):
    if pattern.match(data):
        op1, op2 = data.split(', ')
        return str(int(op1) + int(op2))
    else:
        return 'Match Error. Struct for operation queue_name, op, op with spaces.'

def on_request(ch, method, props, body):
    data = str(body)

    print(" [.] sum(%s)" % data)
    response = sum(data)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='+')

print(" [x] Awaiting RPC requests")
channel.start_consuming()