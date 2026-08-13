import requests


def get_btc_price():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "bitcoin", "vs_currencies": "usd"}
    )
    data = response.json()
    print(data["bitcoin"]["usd"])
get_btc_price()
