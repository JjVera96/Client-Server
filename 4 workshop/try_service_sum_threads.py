import socket

HOST = '192.168.11.157'
PORT = 5500
s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Listening to ip {} in port {}'.format(HOST, PORT))
s_recv.bind((HOST, PORT))
s_recv.listen(10)
conn, addr = s_recv.accept()
print('Connected by', addr)
ip = addr[0]
conn.send(str(1))
op = conn.recv(1024)
print(op)
conn.send(str(ip))
port = conn.recv(1024)
port = int(port)
print(port)

conn.close()

numbers = 10

while numbers:
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.connect((ip, port))
    s_server.send('+,1,2')
    data = s_server.recv(1024)
    print(data)
    s_server.close()
    numbers -= 1
