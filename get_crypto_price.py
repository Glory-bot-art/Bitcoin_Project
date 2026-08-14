import requests

def get_crypto_price(coin, currency):
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin, "vs_currencies": currency},
            timeout=10,
        )
        data = response.json()
        coin = coin.lower()
        currency = currency.lower()

        if coin in data and currency in data[coin]:
            price = data[coin][currency]
            print(f"Current {coin.capitalize()} Price: {price:,.2f} {currency.upper()}")
        else:
            print(f"could not find data for {coin} and {currency}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
if __name__ == "__main__":
    print("Welcome to the Crypto Tracker!")
    user_coin = input("Enter a coin (e.g., bitcoin, solana, dogecoin): ")
    user_currency = input("Enter a currency (e.g., usd, eur, gbp): ")
    
    get_crypto_price(user_coin, user_currency)