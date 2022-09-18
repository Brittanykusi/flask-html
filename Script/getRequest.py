import requests

url = 'https://www.google.com'

myHeaders =  {'content-type':'html/text'}

response = requests.get(url, headers=myHeaders)

response.status_code

response.json()