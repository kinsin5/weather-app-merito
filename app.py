from flask import Flask, render_template, request

from services.database_service import (
    DatabaseServiceError,
    get_recent_searches,
    initialize_database,
    save_weather,
    seed_default_cities,
)
from services.weather_service import WeatherServiceError, get_current_weather


app = Flask(__name__)
initialize_database()
startup_errors = seed_default_cities()


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""
    recent_searches = []
    database_error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Wpisz nazwe miasta."
        else:
            try:
                weather = get_current_weather(city)
                save_weather(weather)
            except WeatherServiceError as exc:
                error = str(exc)
            except DatabaseServiceError as exc:
                error = str(exc)

    try:
        recent_searches = get_recent_searches()
    except DatabaseServiceError as exc:
        database_error = str(exc)

    return render_template(
        "index.html",
        city=city,
        weather=weather,
        recent_searches=recent_searches,
        error=error,
        database_error=database_error,
        startup_errors=startup_errors,
    )


if __name__ == "__main__":
    app.run(debug=True)
