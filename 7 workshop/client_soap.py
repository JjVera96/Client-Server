
from suds.client import Client

client = Client('http://localhost:8000/?wsdl', cache=None)
print(client.service.say_hello(u'Hola', 5))
