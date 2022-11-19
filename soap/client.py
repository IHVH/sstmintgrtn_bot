from zeep import Client

client = Client('http://localhost:8000/?wsdl')
result = client.service.say_hello()

print(result)