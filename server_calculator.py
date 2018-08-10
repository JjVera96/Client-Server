import socket

HOST = '192.168.10.185'
PORT = 50002           # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Listening to ip {} in port {}'.format(HOST, PORT)
s.bind((HOST, PORT))
s.listen(10)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        if not data: break
        if ',' in data:
            operation, op1, op2 = data.split(',')
            if operation == '+':
                result = int(op1) + int(op2)
            else:
                result = 'Match Error. Operation not supported'
        else:
            result = 'Match Error. Operation not supported'
        conn.send(str(result))
conn.close()
