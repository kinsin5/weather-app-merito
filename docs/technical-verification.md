# Weryfikacja techniczna projektu WeatherApp

## Lokalizacja najwazniejszych elementow

- Specyfikacja projektu: `README.md`, sekcje 1-11.
- Dokumentacja techniczna: `README.md`, sekcja 13 oraz `docs/feature-api-database-view.md`.
- Kod odpowiedzialny za API: `services/weather_service.py`.
- Kod odpowiedzialny za SQLite: `services/database_service.py`.
- Warstwa widoku: `templates/index.html`.
- Style widoku: `static/style.css`.
- Glowna logika aplikacji Flask: `app.py`.
- Lista kontrolna do sprawdzenia: `sprawdzenie.md`.

## Realizacja wymagan funkcjonalnych

1. Wpisanie nazwy miasta: formularz `POST` w `templates/index.html`, obsluga w `app.py`.
2. Pobranie wspolrzednych: funkcja `_get_location` w `services/weather_service.py`.
3. Pobranie pogody: funkcja `_get_weather` w `services/weather_service.py`.
4. Wyswietlenie pogody: blok `weather` w `templates/index.html`.
5. Bledna nazwa miasta: `WeatherServiceError` z komunikatem "Nie znaleziono podanego miasta.".
6. Blad polaczenia z API: obsluga `requests.RequestException` w `services/weather_service.py`.
7. Ponowne wyszukanie bez restartu: formularz dziala na endpoint `/` w metodzie `POST`.
8. Historia SQLite: `save_weather` zapisuje kazde poprawne wyszukanie w tabeli `weather_history`.
9. Ostatnie wyszukiwania: `get_recent_searches` pobiera ostatnie rekordy i przekazuje je do widoku.

## Struktura projektu

Projekt ma podzial na:

- routing i kontroler aplikacji: `app.py`,
- logike API: `services/weather_service.py`,
- logike bazy danych: `services/database_service.py`,
- HTML: `templates/index.html`,
- CSS: `static/style.css`,
- dokumentacje: `README.md` i `docs/`.

Taki podzial pokazuje separacje logiki od widoku. Szablon HTML wyswietla dane, ale nie pobiera ich z API ani nie wykonuje operacji bazodanowych.

## SQLite

Projekt zawiera baze SQLite w `database/weather.db`. Przy starcie aplikacji tworzona jest tabela `weather_history`, jezeli jeszcze nie istnieje.

Tabela przechowuje:

- `id`
- `city`
- `country`
- `temperature`
- `feels_like`
- `humidity`
- `wind_speed`
- `searched_at`

Przy pierwszym starcie aplikacja pobiera dane dla 10 najwiekszych miast w Polsce i zapisuje je jako poczatkowa historie.

## Ocena projektu

Poprawne elementy:

- Projekt ma czytelna strukture katalogow.
- Logika API jest oddzielona od widoku.
- Logika SQLite jest oddzielona od aplikacji Flask.
- Widok webowy ma formularz, wynik pogody, komunikaty bledow i ostatnie wyszukiwania.
- Baza danych jest tworzona automatycznie.
- Projekt ma `requirements.txt` i instrukcje uruchomienia.

Co warto poprawic:

- Dodac testy jednostkowe dla `weather_service.py` i `database_service.py`.
- Dodac formatowanie daty `searched_at` na bardziej czytelne dla uzytkownika.
- W przyszlosci mozna ograniczyc seedowanie do osobnej komendy administracyjnej.

Czy projekt spelnia wymagania techniczne na zaliczenie:

Tak. Projekt spelnia wymagania dotyczace Flask, API pogodowego, SQLite, widoku webowego, separacji logiki, obslugi bledow, dokumentacji i lokalnego uruchamiania.

## Co pokazac prowadzacemu

1. `README.md` jako specyfikacje i dokumentacje techniczna.
2. `app.py`, zeby pokazac routing i przeplyw formularza.
3. `services/weather_service.py`, zeby pokazac polaczenie z Open-Meteo.
4. `services/database_service.py`, zeby pokazac tworzenie tabeli, seed i zapis historii.
5. `templates/index.html`, zeby pokazac oddzielona warstwe widoku.
6. Dzialajaca aplikacje pod `http://127.0.0.1:5000`.
7. Wyszukanie poprawnego miasta, np. `Warszawa`.
8. Wyszukanie blednej nazwy miasta, zeby pokazac obsluge bledow.
9. Sekcje "Ostatnie wyszukiwania", zeby pokazac dane z SQLite.
