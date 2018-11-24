import socket

HOST = '192.168.17.12'
PORT = 50002
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    envio = raw_input('Send to Server: ')
    if envio == '':
        print 'Goodbye Little Bitch'
        break
    s.connect((HOST, PORT))
    s.send(envio)
    data = s.recv(1024)
    print 'Received', repr(data)
    s.close()
