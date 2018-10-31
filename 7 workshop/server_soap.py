from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from spyne.protocol.http import HttpRpc
from spyne import ServiceBase, Integer, rpc, Application, Unicode, ValidationError, Iterable

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))

    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name

application = Application([HelloWorldService],
                        tns='spyne.examples.hello',
                        in_protocol=HttpRpc(validator='soft'),
                        out_protocol=Soap11())

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
