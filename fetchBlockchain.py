import requests
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def fetch_blockchain_stats():
    # Define the URL of the API endpoint
    url = "https://api.blockchain.info/stats"

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON content of the response to the terminal
        print(response.json())
    else:
        # Print an error message to the terminal
        print(f"Error: Received status code {response.status_code} from API")

# Call the function
# fetch_blockchain_stats()

def getL2OrderBook(symbol):
    # Define the URL of the API endpoint
    url = f"https://api.blockchain.com/v3/exchange/l2/{symbol}"

    # Define the headers
    headers = {"Accept": "application/json", "X-API-Token": os.getenv('X_API_TOKEN')}

    # Make a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON content of the response to the terminal
        print(response.json())
    else:
        # Print an error message to the terminal
        print(f"Error: Received status code {response.status_code} from API")

def getL3OrderBook(symbol):
    # Define the URL of the API endpoint
    url = f"https://api.blockchain.com/v3/exchange/l3/{symbol}"

    # Define the headers
    headers = {"Accept": "application/json", "X-API-Token": os.getenv('X_API_TOKEN')}

    # Make a GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON content of the response to the terminal
        print(response.json())
    else:
        # Print an error message to the terminal
        print(f"Error: Received status code {response.status_code} from API")

#getL2OrderBook("BTC-USD")
#getL3OrderBook("BTC-USD")

def get_chart_data(chart_name, timespan, rolling_average, start, format):
    # Define the URL of the API endpoint
    url = f"https://api.blockchain.info/charts/{chart_name}?timespan={timespan}&format={format}"
    
    if rolling_average:
        url += f"&rollingAverage={rolling_average}"
    
    if start:
        url += f"&start={start}"

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON content of the response
        return response.json()
    else:
        # Print an error message to the terminal
        print(f"Error: Received status code {response.status_code} from API")
        return None

# get_chart_data("mempool-size", "1week", "24hours", "json")
# print(get_chart_data("miners-revenue", "1year", "", "2023-04-28", "json"))


"""
True means that the 30-day moving average is greater than the 60-day moving average. In the context of hash ribbons, this is often interpreted as a "buy" signal, suggesting that it might be a good time to buy Bitcoin.
False means that the 30-day moving average is less than or equal to the 60-day moving average. This is often interpreted as a "sell" signal, suggesting that it might b
"""
def calculate_hash_ribbons():
    # Get the hash rate data with 30-day and 60-day rolling averages
    hash_rate_30 = get_chart_data("hash-rate", "1year", "30days", "2023-04-28", "json")
    hash_rate_60 = get_chart_data("hash-rate", "1year", "60days", "2023-04-28", "json")

    # Convert the data to pandas DataFrames
    df_30 = pd.DataFrame(hash_rate_30['values'])
    df_60 = pd.DataFrame(hash_rate_60['values'])

    # Calculate the moving averages
    df_30['MA'] = df_30['y'].rolling(window=30).mean()
    df_60['MA'] = df_60['y'].rolling(window=60).mean()

    # Calculate the difference between the two averages
    difference = df_30['MA'] - df_60['MA']

    return difference

difference = calculate_hash_ribbons()
print(difference)