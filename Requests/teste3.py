import requests

data = {'key': 'value'}
response = requests.post('https://api.exemplo.com/enviar', data=data)
print(response.json())
