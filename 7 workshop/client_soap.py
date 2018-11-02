from suds.client import Client

client = Client('http://192.168.1.63:8000/?wsdl', cache=None)
print(client.service.sum(4, 5))
