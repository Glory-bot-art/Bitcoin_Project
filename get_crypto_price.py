import requests

def get_crypto_price(coin, currency):
    """
    Fetches the current price of a cryptocurrency from CoinGecko.
    """
    coin = coin.lower().strip()
    currency = currency.lower().strip()

    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin, "vs_currencies": currency},
            timeout=10,
        )

        if response.status_code == 200:
            data = response.json()

            if coin in data and currency in data[coin]:
                price = data[coin][currency]
                print(f"Current {coin.capitalize()} Price: {price:,.2f} {currency.upper()}")
            else:
                print(f"❌ Could not find data for '{coin}' in '{currency}'. Check your spelling!")

        elif response.status_code == 429:
            print("🚨 CoinGecko is rate-limiting us. Slow down!")

        else:
            print(f"⚠️ Something went wrong. Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("🔌 No internet! Please check your network connection.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error occurred: {e}")


if __name__ == "__main__":
    print("Welcome to the Crypto Tracker!")
    user_coin = input("Enter a coin (e.g., bitcoin, solana, dogecoin): ")
    user_currency = input("Enter a currency (e.g., usd, eur, gbp): ")

    get_crypto_price(user_coin, user_currency)