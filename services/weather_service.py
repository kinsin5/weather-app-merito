from datetime import datetime, timezone

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherServiceError(Exception):
    """Blad pobierania lub przygotowania danych pogodowych."""


def get_current_weather(city):
    location = _get_location(city)
    weather = _get_weather(location["latitude"], location["longitude"])

    return {
        "city": location["name"],
        "country": location.get("country", ""),
        "temperature": weather["temperature_2m"],
        "feels_like": weather["apparent_temperature"],
        "humidity": weather["relative_humidity_2m"],
        "wind_speed": weather["wind_speed_10m"],
        "searched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def _get_location(city):
    try:
        response = requests.get(
            GEOCODING_URL,
            params={"name": city, "count": 1, "language": "pl", "format": "json"},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise WeatherServiceError("Nie udalo sie polaczyc z API lokalizacji.") from exc

    results = response.json().get("results", [])
    if not results:
        raise WeatherServiceError("Nie znaleziono podanego miasta.")

    return results[0]


def _get_weather(latitude, longitude):
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,apparent_temperature,"
                    "relative_humidity_2m,wind_speed_10m"
                ),
            },
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise WeatherServiceError("Nie udalo sie pobrac danych pogodowych.") from exc

    current = response.json().get("current")
    if not current:
        raise WeatherServiceError("API pogodowe nie zwrocilo aktualnych danych.")

    return current
