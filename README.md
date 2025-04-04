# Integrationstestning i Python (Flask + SQLite)

Välkommen till denna övning i integrationstestning. Du kommer att jobba med en enkel Flask-app vars REST API hanterar anteckningar i en databas. Din uppgift är att förstå hur integrationstester fungerar och att själv skriva tester med hjälp av `pytest`.

## Syfte

- Förstå hur integrationstest skiljer sig från enhetstest och systemtest.
- Lära dig hur du testar en app där flera komponenter (API + databas) samverkar.
- Skriva tydliga och verifierbara tester.


## Kom igång

1. Skapa ett virtuellt Python-miljö (valfritt men rekommenderas):

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate.ps1   # Windows (PowerShell)
```

2. Installera beroenden:

```bash
pip install -r requirements.txt
```

3. Kör tester:

```bash
pytest
```

Du bör se minst ett test som körs – sen är det din tur att lägga till fler!

## Projektet filstruktur

```plaintext
.
├── app/                # Flask-applikationen
│   └── app.py          # Flask-routes och logik
│   └── main.py         # Startar appen (används ej i test)
├── tests/
│   └── integration/
│       └── test_app.py # Här skriver du dina tester!
├── db/                 # Katalog där databasfiler kommer lagras
```

## Din uppgift

I [tests/integration/test_app.py](./tests/integration/test_app.py) hittar du:
- Ett färdigt test  
- Flera delvis eller helt tomma testfunktioner med beskrivningar

Övningens steg:
1. Läs koden i [app/app.py](./app/app.py).
2. Utforska APIet manuellt med hjälp av verktyget Postman. Gör förberedelserna och **endast Del 1** [här](./postman/README.md).
3. Bekanta dig med testkoden i [tests/integration/test_app.py](./tests/integration/test_app.py) och förstå hur den funkar.
4. Implementera testfunktioner med TODO kommentarer.
    - Använd `hamcrest`-matchers för alla assert-satser.
    - (Bonus) Skriv ett (eller flera) testfall baserat på din tolkning av appen.

## Verktyg/moduler som används

- [Flask](https://flask.palletsprojects.com/): Webbramverk för API:et
- [SQLite](https://docs.python.org/3/library/sqlite3.html): Enkel filbaserad databas
- [Pytest](https://docs.pytest.org/): Ramverk för testkörning
- [Pyhamcrest](https://pypi.org/project/PyHamcrest/): Läsbara assertion-matchers

## Tips för bra tester

- Använd tydliga testnamn som visar **vad** du testar och **vad som förväntas**.
- Strukturera testet med kommentarer:
  ```python
  # GIVEN ...
  # WHEN ...
  # THEN ...
  ```
- Skriv inte testfall som beror av andra testfall.
- Använd inte konstanter eller variabler som kommer från den kod som ska testas.
- Skriv hellre **flera mindre tester** än ett stort.
