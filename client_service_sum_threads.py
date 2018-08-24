import socket

ip = '192.168.17.12'
port = 50000

numbers = 10
while numbers:
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.connect((ip, port))
    s_server.send('+,4,5'.encode('ascii'))
    data = s_server.recv(1024).decode('ascii')
    print(data)
    s_server.close()
    numbers -= 1
