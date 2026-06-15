import sqlite3
from pathlib import Path

from services.weather_service import WeatherServiceError, get_current_weather


DATABASE_PATH = Path(__file__).resolve().parent.parent / "database" / "weather.db"

DEFAULT_CITIES = [
    "Warszawa",
    "Kraków",
    "Łódź",
    "Wrocław",
    "Poznań",
    "Gdańsk",
    "Szczecin",
    "Bydgoszcz",
    "Lublin",
    "Białystok",
]


class DatabaseServiceError(Exception):
    """Blad zapisu lub odczytu danych z bazy SQLite."""


def initialize_database():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with _connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS weather_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                country TEXT,
                temperature REAL NOT NULL,
                feels_like REAL NOT NULL,
                humidity INTEGER NOT NULL,
                wind_speed REAL NOT NULL,
                searched_at TEXT NOT NULL
            )
            """
        )


def seed_default_cities():
    errors = []
    saved_cities = _get_saved_cities()

    for city in DEFAULT_CITIES:
        if city.casefold() in saved_cities:
            continue

        try:
            weather = get_current_weather(city)
            save_weather(weather)
        except (WeatherServiceError, DatabaseServiceError) as exc:
            errors.append(f"{city}: {exc}")

    return errors


def save_weather(weather):
    try:
        with _connect() as connection:
            connection.execute(
                """
                INSERT INTO weather_history (
                    city, country, temperature, feels_like, humidity,
                    wind_speed, searched_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    weather["city"],
                    weather.get("country", ""),
                    weather["temperature"],
                    weather["feels_like"],
                    weather["humidity"],
                    weather["wind_speed"],
                    weather["searched_at"],
                ),
            )
    except sqlite3.Error as exc:
        raise DatabaseServiceError("Nie udalo sie zapisac danych w bazie.") from exc


def get_saved_weather():
    return get_recent_searches()


def get_recent_searches(limit=10):
    try:
        with _connect() as connection:
            rows = connection.execute(
                """
                SELECT city, country, temperature, feels_like, humidity,
                       wind_speed, searched_at
                FROM weather_history
                ORDER BY searched_at DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
    except sqlite3.Error as exc:
        raise DatabaseServiceError("Nie udalo sie odczytac danych z bazy.") from exc

    return [_row_to_weather(row) for row in rows]


def _get_saved_cities():
    try:
        with _connect() as connection:
            rows = connection.execute(
                "SELECT DISTINCT city FROM weather_history"
            ).fetchall()
    except sqlite3.Error as exc:
        raise DatabaseServiceError("Nie udalo sie sprawdzic historii pogody.") from exc

    return {row["city"].casefold() for row in rows}



def _connect():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def _row_to_weather(row):
    return {
        "city": row["city"],
        "country": row["country"],
        "temperature": row["temperature"],
        "feels_like": row["feels_like"],
        "humidity": row["humidity"],
        "wind_speed": row["wind_speed"],
        "searched_at": row["searched_at"],
    }
