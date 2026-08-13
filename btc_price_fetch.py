import requests


def get_btc_price():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "bitcoin", "vs_currencies": "usd"}
    )
    data = response.json()
    print(data["bitcoin"]["usd"])


#try/except for network failure
try:
    get_btc_price()
except:
    print("No internet! Please connect to a network.")
    
