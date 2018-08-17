import socket

HOST = '192.168.1.65'
PORT = 5555
s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Listening to ip {} in port {}'.format(HOST, PORT))
s_recv.bind((HOST, PORT))
s_recv.listen(10)
conn, addr = s_recv.accept()
print('Connected by', addr)
ip = addr[0]
data = conn.recv(1024).decode('ascii')
op, port = data.split(',')
port = int(port)
conn.send(ip.encode('ascii'))
conn.close()

while True:
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.connect((ip, port))
    s_server.send('+,5,3'.encode('ascii'))
    data = s_server.recv(1024).decode('ascii')
    print(data)
    s_server.close()
