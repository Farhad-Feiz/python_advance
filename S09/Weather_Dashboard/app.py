from flask import Flask, render_template, request

from weather_api import get_weather
from model import SearchHistory, db


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    db.connect(reuse_if_open=True)

    weather = None
    error = None

    if request.method == "POST":

        city = request.form["city"]

        weather = get_weather(city)

        if weather is None:

            error = "City not found. Please enter a valid city name."

        else:

            SearchHistory.create(
                city_name=city
            )

    searches = list(
        SearchHistory
        .select()
        .order_by(
            SearchHistory.search_date.desc()
        )
    )

    db.close()

    return render_template(
        "weather.html",
        weather=weather,
        searches=searches,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)