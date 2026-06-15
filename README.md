# weather-app-merito
Project for my Jezyki Programowania final project 

Polish specification below :)

# Specyfikacja projektu - WeatherApp

## 1. Krótki opis projektu

Celem projektu jest stworzenie prostej aplikacji webowej umożliwiającej sprawdzenie aktualnej pogody dla wybranego miasta. Użytkownik wpisuje nazwę miejscowości w formularzu, a system pobiera dane z zewnętrznego API pogodowego i prezentuje je w czytelnej formie na stronie internetowej.

Projekt zostanie wykonany w języku Python z wykorzystaniem frameworka Flask. Warstwa widoku zostanie przygotowana przy użyciu HTML i CSS, natomiast logika pobierania danych pogodowych zostanie wydzielona do osobnego modułu aplikacji.

## 2. Cel projektu

Celem aplikacji jest umożliwienie szybkiego sprawdzenia podstawowych informacji pogodowych bez konieczności korzystania z wielu różnych serwisów internetowych. Aplikacja ma być prosta, czytelna i łatwa w obsłudze.

## 3. Wymagania funkcjonalne

1. System umożliwia użytkownikowi wpisanie nazwy miasta w formularzu wyszukiwania.
2. System pobiera współrzędne geograficzne miasta na podstawie wpisanej nazwy.
3. System pobiera aktualne dane pogodowe z zewnętrznego API.
4. System wyświetla użytkownikowi podstawowe informacje pogodowe, takie jak temperatura, temperatura odczuwalna, wilgotność oraz prędkość wiatru.
5. System informuje użytkownika o błędzie, jeżeli wpisane miasto nie zostanie znalezione.
6. System informuje użytkownika o błędzie, jeżeli wystąpi problem z połączeniem z API pogodowym.
7. System umożliwia ponowne wyszukanie pogody dla innego miasta bez konieczności restartowania aplikacji.

## 5. Wymagania pozafunkcjonalne

1. Aplikacja powinna działać lokalnie w przeglądarce internetowej.
2. Interfejs użytkownika powinien być prosty, czytelny i intuicyjny.
3. Kod aplikacji powinien być podzielony na warstwę widoku oraz warstwę logiki aplikacji.
4. Nazwy plików, funkcji i zmiennych powinny być zgodne z podstawowymi konwencjami języka Python.

## 6. Potencjalni odbiorcy systemu

1. Osoby, które chcą szybko sprawdzić aktualną pogodę w swoim mieście.
2. Użytkownicy, którzy potrzebują prostego narzędzia do sprawdzania podstawowych informacji pogodowych.

## 7. Korzyści dla użytkowników końcowych

1. Szybki dostęp do aktualnych informacji pogodowych.
2. Prosty i czytelny sposób prezentacji danych.
3. Brak konieczności instalowania dodatkowej aplikacji system działa w przeglądarce.

## 8. Technologie

* Python
* Flask
* HTML
* CSS
* requests
* SQLite
* Open-Meteo API

## 9. Zakres projektu

W podstawowym zakresie aplikacja będzie umożliwiała wyszukanie miasta i wyświetlenie aktualnej pogody. Projekt nie będzie systemem produkcyjnym, lecz prostą aplikacją edukacyjną pokazującą wykorzystanie języka Python, frameworka Flask, zewnętrznego API oraz podziału kodu na logiczne części.

## 10. Planowana struktura aplikacji

DODAJ STRUKTURE!!

```
weather-app-flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── weather.db
│
├── services/
│   ├── weather_service.py
│   └── history_service.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── docs/
    └── specyfikacja.md
```

## 11. Separacja logiki od widoku

Projekt będzie posiadał prosty podział odpowiedzialności:

* plik `app.py` będzie odpowiadał za uruchomienie aplikacji Flask oraz obsługę żądań użytkownika,
* plik `weather_service.py` będzie odpowiadał za komunikację z API pogodowym i przygotowanie danych,
* pliki HTML w katalogu `templates` będą odpowiadały za prezentację danych użytkownikowi,
* plik CSS w katalogu `static` będzie odpowiadał za wygląd aplikacji.

Dzięki temu kod będzie czytelniejszy, łatwiejszy do utrzymania i zgodny z zasadą oddzielenia logiki aplikacji od warstwy widoku.


## 12. RUN:

.\.venv\Scripts\python.exe -m flask --app app run --host 127.0.0.1 --port 5000 --no-reload

## 13. Dokumentacja techniczna

### Uruchomienie lokalne

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Po uruchomieniu aplikacja dziala pod adresem:

```text
http://127.0.0.1:5000
```

### Aktualna struktura katalogow

```text
weather-app-merito/
|-- app.py
|-- requirements.txt
|-- README.md
|-- sprawdzenie.md
|-- database/
|   `-- weather.db
|-- docs/
|   |-- feature-api-database-view.md
|   `-- technical-verification.md
|-- services/
|   |-- __init__.py
|   |-- database_service.py
|   `-- weather_service.py
|-- static/
|   `-- style.css
`-- templates/
    `-- index.html
```

### Podstawowe funkcje aplikacji

1. Uzytkownik wpisuje nazwe miasta w formularzu na stronie glownej.
2. Aplikacja pobiera wspolrzedne miasta z Open-Meteo Geocoding API.
3. Aplikacja pobiera aktualna pogode z Open-Meteo Forecast API.
4. Wynik jest wyswietlany w widoku webowym.
5. Kazde poprawne wyszukanie jest zapisywane w historii SQLite.
6. Przy pierwszym starcie aplikacja zapisuje dane dla 10 najwiekszych miast w Polsce.
7. Strona pokazuje ostatnie wyszukiwania zapisane w bazie.
8. Aplikacja wyswietla komunikaty bledow dla pustego formularza, nieznanego miasta, problemow z API i problemow z baza danych.

### Struktura bazy SQLite

Baza danych znajduje sie w pliku `database/weather.db`. Tabela `weather_history` jest tworzona automatycznie przy starcie aplikacji.

Kolumny tabeli:

| Kolumna | Typ | Opis |
| --- | --- | --- |
| `id` | INTEGER | Klucz glowny rekordu historii |
| `city` | TEXT | Nazwa miasta |
| `country` | TEXT | Nazwa kraju |
| `temperature` | REAL | Aktualna temperatura |
| `feels_like` | REAL | Temperatura odczuwalna |
| `humidity` | INTEGER | Wilgotnosc |
| `wind_speed` | REAL | Predkosc wiatru |
| `searched_at` | TEXT | Data i czas pobrania danych |

### Separacja odpowiedzialnosci

- `app.py` odpowiada za routing Flask, obsluge formularza i przekazywanie danych do widoku.
- `services/weather_service.py` odpowiada za polaczenie z API pogodowym.
- `services/database_service.py` odpowiada za SQLite, seed danych i historie wyszukiwan.
- `templates/index.html` odpowiada za warstwe widoku.
- `static/style.css` odpowiada za wyglad aplikacji.
