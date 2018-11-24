from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from spyne.protocol.http import HttpRpc
from spyne import ServiceBase, Integer, rpc, Application, Unicode, Iterable
from wsgiref.simple_server import make_server

class SumService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)

    def sum(ctx, op1, op2):
        result = op1 + op2
        return result

application = Application([SumService], tns='cs.sum', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    server = make_server('192.168.1.63', 8000, wsgi_app)
    server.serve_forever()
