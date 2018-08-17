import socket

HOST_MIDDLEWARE = '192.168.11.157'
PORT_MIDDLEWARE  = 5555

s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_server.connect((HOST_MIDDLEWARE, PORT_MIDDLEWARE))
#data = s_server.recv(1024)
#print(data)
s_server.send('+')
while True:
    result = ''
    data = s_server.recv(1024)
    print(data)
    if ',' in data:
        operation, op1, op2 = data.split(',')
        if operation == '+':
            result = int(op1) + int(op2)
        else:
            result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
    else:
        result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
    s_server.send(str(result))
s_server.close()
