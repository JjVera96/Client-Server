from suds.client import Client

client = Client('http://10.253.22.235:8000/?wsdl', cache=None)

while True:
	x = input('Input number x: ')
	if x == '': break
	y = input('Input number y: ')
	print(client.service.sum(x, y))