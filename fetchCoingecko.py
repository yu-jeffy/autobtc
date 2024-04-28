import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

COINGECKO_API_KEY = os.getenv('COINGECKO_API_KEY')

def call_api(endpoint, api_key, params=None):
    base_url = "https://api.coingecko.com/api/v3/"
    if params and 'id' in params:
        endpoint = endpoint.replace('{id}', params['id'])
    full_url = base_url + endpoint
    headers = {"x-cg-demo-api-key": api_key}
    
    response = requests.get(full_url, headers=headers, params=params)
    
    return response.json()

response = call_api("/coins/{id}/history?date=27-04-2024", COINGECKO_API_KEY, {"id": "bitcoin"})

# Save response to a JSON file
with open('response.json', 'w') as file:
    json.dump(response, file)


# Extract the price and volume for USD
price_usd = response.get('market_data', {}).get('current_price', {}).get('usd')
volume_usd = response.get('market_data', {}).get('total_volume', {}).get('usd')

print(f'Price (USD): {price_usd}')
print(f'Volume (USD): {volume_usd}')

print(response)