from flask import Flask, render_template, request

from services.weather_service import WeatherServiceError, get_current_weather


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Wpisz nazwe miasta."
        else:
            try:
                weather = get_current_weather(city)
            except WeatherServiceError as exc:
                error = str(exc)

    return render_template("index.html", city=city, weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
