from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.model import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.service import ServiceBase

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx):
        return("A")

application = Application([HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='soft'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()