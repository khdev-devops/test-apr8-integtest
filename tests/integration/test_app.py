import pytest
import os
from app import create_app
from hamcrest import assert_that, equal_to, contains_string

TEST_DB = "db/test.db"

# Se till att databasens mapp finns
os.makedirs("db", exist_ok=True)


@pytest.fixture
def client():
    # Radera ev. tidigare testdatabas
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    app = create_app(TEST_DB)
    app.init_db()

    with app.test_client() as client:
        yield client

    # Rensa efter testet
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_get_should_return_empty_list_when_no_notes(client):
    # GIVEN inga anteckningar
    # WHEN vi hämtar startsidan
    resp = client.get("/")

    # THEN ska svaret vara tomt
    assert_that(resp.status_code, equal_to(200))
    assert_that(resp.data.decode("utf-8"), equal_to(""))


# TODO: skriv dit kod som testar det som beskrivs i GIVEN, WHEN, THEN
def test_add_and_get_note_should_store_and_return_text(client):
    # GIVEN att inga anteckningar finns
    # WHEN vi lägger till en ny anteckning
    # THEN ska anteckningen synas när vi hämtar alla
    pass


# TODO: skriv dit GIVEN, WHEN och THEN samt kod som testar det som beskrivs
def test_add_note_should_fail_without_text(client):
    # GIVEN ...
    # WHEN ...
    # THEN ...
    pass


# TODO: skriv ett eget (eller flera testfall)
def test_bonus():
    # GIVEN ...
    # WHEN ...
    # THEN ...
    pass
