import socket
import threading

class Sum():
    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))

    def


def main():
    PORT = 50002
    HOST_MIDDLEWARE = '192.168.11.157'
    PORT_MIDDLEWARE  = 5555

    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.connect((HOST_MIDDLEWARE, PORT_MIDDLEWARE))
    s_server.send('+,{}'.format(PORT))
    ip = s_server.recv(1024)
    s_server.close()
    print(ip)
    sum = Sum(ip, PORT)





if __name__ == '__main__':
    main()
