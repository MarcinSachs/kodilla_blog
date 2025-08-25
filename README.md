# blog

## Opis

Projekt prostego bloga zbudowanego przy użyciu Flaska. Umożliwia tworzenie, edycję i publikowanie postów.

## Screenshot

![screenshot.png](screenshot.png)

## Live Demo

[https://927fcd1e-dea7-4b7c-93d8-c10b8db2c3e4-00-547jwc9djwyt.janeway.replit.dev/](https://927fcd1e-dea7-4b7c-93d8-c10b8db2c3e4-00-547jwc9djwyt.janeway.replit.dev/)

## Uruchomienie lokalne

1.  Sklonuj repozytorium:

    ```bash
    git clone [adres twojego repozytorium]
    cd blog
    ```

2.  Utwórz i aktywuj środowisko wirtualne (opcjonalne, ale zalecane):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

3.  Zainstaluj zależności:

    ```bash
    pip install -r requirements.txt
    ```

4.  Ustaw zmienną środowiskową `FLASK_APP`:

    ```bash
    export FLASK_APP=blog:app  # Linux/macOS
    # set FLASK_APP=blog:app    # Windows
    ```

5.  Uruchom serwer Flask:

    ```bash
    flask run --debug
    ```

    Otwórz w przeglądarce adres wyświetlony w konsoli (zazwyczaj `http://127.0.0.1:5000`).

## Konfiguracja

*   **Zmienne środowiskowe:** Projekt korzysta ze zmiennych środowiskowych. Upewnij się, że masz ustawione następujące zmienne:
    *   `SECRET_KEY`: Klucz używany do ochrony sesji. Powinien być ustawiony na losowy ciąg znaków.
    *   `ADMIN_USERNAME`: Nazwa użytkownika administratora.
    *   `ADMIN_PASSWORD`: Hasło administratora.
    *   `SQLALCHEMY_DATABASE_URI`: Adres URL bazy danych. Jeśli nie ustawisz tej zmiennej, domyślnie używana będzie baza danych SQLite.
        *   Przykład SQLite: `sqlite:///database.db`
        *   Przykład PostgreSQL: `postgresql://user:password@host:port/database`

## Migracje bazy danych

Projekt używa Flask-Migrate do zarządzania migracjami bazy danych.

1.  Zainicjalizuj migracje (tylko raz):

    ```bash
    flask db init
    ```

2.  Utwórz migrację:

    ```bash
    flask db migrate -m "Dodaj opis migracji"
    ```

3.  Zastosuj migrację:

    ```bash
    flask db upgrade
    ```
