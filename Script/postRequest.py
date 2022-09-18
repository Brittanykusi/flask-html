import requests

url = "https://httpbin.org/post"

data = {'id': 1001, 'name': 'brittany', ' passion': 'coding'}

response = requests.post(url,json=data)

print('Status Code', response.status_code)
print('JSON RESPONSE', response.json())