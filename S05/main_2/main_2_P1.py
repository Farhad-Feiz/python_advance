import requests

key = "e982bd7cf47f46ae9076908212558e81"
url = f"https://api.spoonacular.com/recipes/findByIngredients"

ingredients = input(
    "Enter 3 ingredients separated by commas: "
)

params = {
    "ingredients": ingredients,
    "number": 1,
    "apiKey": key
}

res= requests.get(url,params=params)
data = res.json()

if not data:
    print("No recipe found.")
else:
    print(type(data))
    print(data)
    recipe = data[0]

    print("Recipe Title:")
    print(recipe["title"])
    print(data[0]["image"])

    print("\nMissing Ingredients:")

    for item in recipe["missedIngredients"]:
        print("-", item["name"])
    