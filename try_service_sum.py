import socket
import random

HOST = '192.168.8.229'
PORT = 5500
s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Listening to ip {} in port {}'.format(HOST, PORT)
s_recv.bind((HOST, PORT))
s_recv.listen(1)
conn, addr = s_recv.accept()
print 'Connected by', addr
conn.send('Ok')
data = conn.recv(1024)
print(data)
while True:
    op1 = raw_input('First Operator: ')
    op2 = raw_input('Second Operator: ')
    try:
        op1 = int(op1)
        op2 = int(op2)
    except ValueError:
        print "Warning: You must enter integers numbers."
        op1 = None
        op2 = None
    if op1 is not None:
        conn.send('+,{},{}'.format(op1, op2))
        data = conn.recv(1024)
        print('Result: {}'.format(data))
conn.close()
