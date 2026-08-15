import requests


def get_btc_price():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin", "vs_currencies": "usd"},
            timeout=10,
        )

        if response.status_code == 200:
            data = response.json()
            print(f"Current Bitcoin Price: ${data['bitcoin']['usd']:,.2f}")

        elif response.status_code == 429:
            print("🚨 CoinGecko is rate-limiting us. Slow down!")

        else:
            print(f"⚠️ Something went wrong. Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("🔌 No internet! Please check your network connection.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error occurred: {e}")

get_btc_price()
