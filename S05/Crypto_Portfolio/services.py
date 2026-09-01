import requests
from portfolio_db import Asset,TradeHistory


def get_price(symbol):

    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol"
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data =response.json()
        return  float(data["price"])
    except(
        requests.exceptions.RequestException,
        KeyError,
        ValueError
    ):
        return None
    
def buy_asset(symbol,amount,price):
    asset = Asset.get_or_none(Asset.symbol==symbol)
    if not asset:
        asset=Asset.create(
            symbol       = symbol,
            total_amount = 0,
            average_price= 0
        )
    old_amount = asset.total_amount
    old_average = asset.average_price
    new_average = (
        (
            old_amount*old_average
        )
        +
        (
            amount*price
        )
    )/(
        amount+old_amount
    )
    asset.total_amount+=amount
    asset.average_price=new_average
    asset.save()

    TradeHistory.create(
        asset=asset,
        trade_type="Buy",
        amount=amount,
        price=price
    )
def sell_asset(
        symbol,
        amount,
        price
):
    asset=Asset.get_or_none(
        Asset.symbol == symbol
    )
    if not asset:
        return False

    if amount>asset.total_amount:
        return False

    asset.total_amount-=amount
    asset.save()

    TradeHistory.create(
        asset = asset,
        amount = amount,
        price=price
    )
    return True
def current_value(symbol):
    asset=Asset.get_or_none
    (
        Asset.symbol==symbol
    )
    if not asset:
        return None
    price = get_price(
        f"{symbol} USDT"
    )
    if price is None:
        return None
    return(
        asset.total_amount
        *
        price
    )
