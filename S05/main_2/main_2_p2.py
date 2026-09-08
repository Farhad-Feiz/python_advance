import requests

url = f"https://newsapi.org/v2/everything"
key = "8b0533f9658d41168e2532a8faf8cc62"

params= {
    "q":"AI",
    "pageSize":5,
    "language":"en"
}
headers = {
    "X-Api-Key": key
    }
response=requests.get(
    url,
    params=params,
    headers=headers
    )
data = response.json()
# print(type(data))
# print(data)

articles = data.get("articles", [])

if not articles:
    print("No news found.")
else:
    # article = articles[:5]
    for article in articles:
        print("Title:")
        print(article["title"])

        print("\nSource:")
        print(article["source"]["name"])
        print("-----------------------")
