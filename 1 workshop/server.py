import socket

HOST = 'localhost'                 # Symbolic name meaning the local host
PORT = 50000           # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Listening to port {}'.format(PORT)
s.bind((HOST, PORT))
s.listen(10)
while True:
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send('Fuck you Doggy. Go to the cock {}'.format(data))
conn.close()
