import requests
url = "pixabay.com/api/docs"
response = requests.get(url)
data  = response.json()
print(data)