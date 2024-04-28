import requests

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']

print(get_public_ip())