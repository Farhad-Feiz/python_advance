import requests
from datetime import date,timedelta

yesterday=(
    date.today()-timedelta(days=1)
).strftime("%Y-%m-%d")
key ="o9pRnGvDx7tLEp6aplnzx6Vitvj4Ws5n"
url= f"https://api.massive.com/v2/aggs/ticker/AAPL/prev?"
params={
    "adjusted":"true",
    "apikey":key
}
response=requests.get(
    url,
    params=params
)
data=response.json()
# print(data)
# print(data["results"][0]["c"])
# print(len(data["results"]))

if "results" in data["results"] and data["results"]:
    close_price= (data["results"][0]["c"])

    print(
        f"AAPL Closed price :{close_price}"
    )
else:
    print("No data was found!")