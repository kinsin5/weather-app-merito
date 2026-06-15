# Feature: API, SQLite i widok webowy

Ten branch dodaje pierwszy pelny przeplyw aplikacji WeatherApp: pobranie danych z API, zapis w bazie SQLite, prezentacje w widoku Flask oraz obsluge bledow.

## Zakres

- Polaczenie z Open-Meteo Geocoding API w celu znalezienia wspolrzednych miasta.
- Polaczenie z Open-Meteo Forecast API w celu pobrania aktualnej pogody.
- Lokalna baza SQLite w pliku `database/weather.db`.
- Automatyczne utworzenie tabeli `weather_records` przy starcie aplikacji.
- Automatyczne pobranie i zapis danych dla 10 najwiekszych miast w Polsce przy pierwszym starcie aplikacji.
- Formularz webowy pozwalajacy wyszukac dowolne miasto.
- Zapis historii wyszukiwan w SQLite.
- Lista ostatnich wyszukiwan widoczna na stronie glownej.
- Komunikaty bledow dla pustego formularza, braku miasta, problemow z API oraz problemow z baza.

## Miasta startowe

Przy starcie aplikacji odswiezane sa dane dla:

1. Warszawa
2. Krakow
3. Lodz
4. Wroclaw
5. Poznan
6. Gdansk
7. Szczecin
8. Bydgoszcz
9. Lublin
10. Bialystok

## Struktura techniczna

- `app.py` obsluguje endpoint `/`, formularz i przekazywanie danych do szablonu.
- `services/weather_service.py` odpowiada za komunikacje z Open-Meteo i mapowanie odpowiedzi API.
- `services/database_service.py` odpowiada za utworzenie SQLite, seed danych startowych, zapis i odczyt rekordow.
- `templates/index.html` renderuje formularz, aktualny wynik, bledy i dane zapisane w bazie.
- `static/style.css` definiuje wyglad formularza, wyniku i listy miast.

## Baza danych

Tabela `weather_history` przechowuje historie wyszukiwan. Kazde wyszukanie miasta dodaje nowy rekord.

Kolumny:

- `id`
- `city`
- `country`
- `temperature`
- `feels_like`
- `humidity`
- `wind_speed`
- `searched_at`

## Uruchomienie

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --host 127.0.0.1 --port 5000 --no-reload
```

Po starcie aplikacja tworzy katalog `database`, plik `weather.db`, tabele i probuje pobrac dane dla miast startowych.
