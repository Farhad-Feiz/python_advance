import requests

key ="f6de299d086f42319dd8d239a3c54895"
url =f"https://ip-intelligence.abstractapi.com/v1"
params={
    "api_key": key
    }
# headers= ...
response = requests.get(
    url,
    params,
    )
data = response.json()
print(type(data))
print(data)
print("Country :",data.get("country"))
print("City :",data.get("city"))
connection=data.get(
    "connection",
    {}
)
print(
    "ISP :",
    connection.get("isp")
)
