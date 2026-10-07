from flask import Flask, render_template, request

from crypto_api import get_crypto_price
from model import CryptoPrice, db


app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "crypto.html",
        coin_name=None,
        price=None,
        prices=[]
    )


@app.route("/crypto")
def crypto_search():

    coin = request.args.get("coin")

    if not coin:
        return render_template(
            "crypto.html",
            coin_name=None,
            price=None,
            prices=[]
        )

    coin = coin.strip().lower()

    return show_crypto(coin)


def show_crypto(coin):

    price = get_crypto_price(coin)

    if price is None:
        return "Coin not found", 404

    db.connect(reuse_if_open=True)

    CryptoPrice.create(
        coin_name=coin,
        price=price
    )

    prices = (
        CryptoPrice
        .select()
        .where(CryptoPrice.coin_name == coin)
        .order_by(CryptoPrice.timestamp.desc())
        .limit(5)
    )

    db.close()

    return render_template(
        "crypto.html",
        coin_name=coin,
        price=price,
        prices=prices
    )


if __name__ == "__main__":
    app.run(debug=True)