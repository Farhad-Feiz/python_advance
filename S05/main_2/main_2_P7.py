import requests

API_Key="5b4fe1c8a88a726a857c6137"
url=f"https://v6.exchangerate-api.com/v6/{API_Key}/latest/EUR"

response=requests.get(
    url,
)
data = response.json()
print(data)