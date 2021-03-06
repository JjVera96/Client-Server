import socket
import threading

class Sum():
    def __init__(self, ip, port, number_connections):
        self.host = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(number_connections)
        print('Server is listening to ip {} in port {}'.format(ip, port))

    def listen(self):
        while True:
            client, address = self.s.accept()
            print('Client connected by: ', address)
            threading.Thread(target = self.operation, args = (client, address)).start()

    def operation(self, client, address):
        while True:
            result = ''
            data = client.recv(1024)
            if not data: break
            print('Operation: {}'.format(data))
            if ',' in data:
                op, op1, op2 = data.split(',')
                if op == '+':
                    result = str(int(op1) + int(op2))
                else:
                    result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
            else:
                result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
            print('Result: {}'.format(result))
            client.send(result)
        client.close()

def main():
    port = 50004
    number_connections = 0
    host_middleware = 'medio.calcseeking.com'
    port_middleware  = 5500
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.connect((host_middleware, port_middleware))
    print('Connected with {} in port {}'.format(host_middleware, port_middleware))
    my_id = s_server.recv(1024)
    print(my_id)
    s_server.send('+')
    ip = s_server.recv(1024)
    print(ip)
    s_server.send(str(port))
    s_server.close()
    print('Socket closed')
    sum = Sum(ip, port, number_connections)
    sum.listen()


if __name__ == '__main__':
    main()
