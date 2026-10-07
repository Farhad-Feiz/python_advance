import requests
import json

from config import GITHUB_API_URL

def get_github_user(username):
    url = f"{GITHUB_API_URL}/{username}"

    response = requests.get(
        url,
        timeout=10
    )
    if response.status_code ==404:
        return None
    response.raise_for_status()

    data = response.json()
    with open("github_user.json", "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )
    print("json file was created successfully!")

    # print(data)

    return{
        "name":data["name"],
        "username":data["login"],
        "followers_count":data["followers"],
        "avatar_url":data["avatar_url"]
    }

if __name__=="__main__":
    
    user=get_github_user("octocat")
    print(user)