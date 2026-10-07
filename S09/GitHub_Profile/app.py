from flask import Flask, render_template
from  github_api import get_github_user
from model import GithubUser,db

app = Flask(__name__)

db.connect(reuse_if_open=True)
db.create_tables([GithubUser])

@app.route("/github/<username>")
def github_profile(username):

    user= GithubUser.get_or_none(
        GithubUser.username== username
    )
    
    
    if user is None:
        data = get_github_user(username)

        if data is None:
            return "Github user not found",404
        
        user = GithubUser.create(
            name=data["name"],
            username= data["username"],
            followers_count=data["followers_count"],
            avatar_url=data["avatar_url"]
        )

    return render_template("profile.html",user=user)
        
if __name__=="__main__":
    app.run(debug=True)