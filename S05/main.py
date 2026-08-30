import requests
import time
"""
# -----------------------------
# .......Age Presumption.......
# -----------------------------

import requests

name = input("Enter a name: ")

url = f"https://api.agify.io/?name={name}"

response = requests.get(url)
data = response.json()

age = data["age"]

print(f"Approximated age for {name} is around {age} years old")

# --------------------------------
#   Random Picture Link Scrapping
# --------------------------------

import requests

url = f"https://dog.ceo/api/breeds/image/random"

response = requests.get(url)
data = response.json()

if data["status"]== "success":
    print("Pic link : ")
    print(data["message"])

# --------------------------------
#   Gender Probability Calculator
# --------------------------------

name = input ("Enter your name : ")

url = f"https://api.genderize.io/?name={name}"

response = requests.get(url)
data = response.json()

print(response.status_code)
print(response.text)

print(data)

gender = data["gender"]
probability = data["probability"]*100

print(f"Gender {gender} with approximation {probability :.2f}")

# --------------------------------
#   Iranian Universities :
# --------------------------------

url = "http://universities.hipolabs.com/search?country=Iran"

response = requests.get(url)
data = response.json()

count = 0

for univerisity in data[:5]:
    print(univerisity["name"])

for i,university in enumerate(data[:5],start = 1`):
    print(i , "---" , university["name"])

#     count +=1

# print("number of universities",{count})

# if count > 0:
#     print("first uiversitty : ")
#     print(data[0],["name"])

# --------------------------------
#   Anti-Boaring Tasks :
# --------------------------------

url = "https://bored-api.appbrewery.com/random"

response = requests.get(url)
data = response.json()

print(data)
participants = data["participants"]
activity = data["activity"]

if participants == 1:
    print(f"Paricipants = {participants}, Activity : {activity}")
    
elif participants >1:
    print(f"Teamwork :{participants} people, Activity : {activity}")

# --------------------------------
#   Nations API :
# --------------------------------

name = input("Enter a name: ")

url = f"https://api.nationalize.io/?name={name}"

response = requests.get(url)
data = response.json()

countries = data["country"]
print(data)

best_countries = max(
    countries, 
    key= lambda item: item["probability"]
    )

print("Highest probabilty", best_countries["country_id"], ["probability"] )
"""
# --------------------------------
#   Two Parts Joke :
# --------------------------------

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
data = response.json()

print(data) 

print(data["setup"])

time.sleep(2)

print(data["punchline"])