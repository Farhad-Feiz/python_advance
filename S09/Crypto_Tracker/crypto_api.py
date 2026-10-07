import requests
from config import COINGECKO_API_URL

def get_crypto_price(coin_name):
    params={
        "ids":coin_name,
        "vs_currencies":"usd"
    }

    response = requests.get(
        COINGECKO_API_URL,
        params=params,
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    if coin_name not in data:
        return None
    return data[coin_name]["usd"]

if __name__=="__main__":
    price = get_crypto_price("bitcoin")
    print(price)