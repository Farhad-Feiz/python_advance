import requests

key ="d7e6e330"
url = f"http://www.omdbapi.com/"

params={
    "apikey":key,
    "t":"Breaking Bad",
    "Season":1
}
response=requests.get(url,params)

data = response.json()
episodes=data["Episodes"]
total = 0
for episode in episodes:
    rating=float(
        episode["imdbRating"]
    )
    total+=rating
average = total/len(episodes)

print(data)
print (type(data))
print (f"Average Rating is : {average:2f}")