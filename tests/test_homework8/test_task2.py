import random

import pytest

from homework8.task2.table_data import TableData

path_to_database = "tests/test_homework8/example.sqlite"

presidents = TableData("tests/test_homework8/example.sqlite", "presidents")
books = TableData("tests/test_homework8/example.sqlite", "books")


def test_len():
    assert len(books) == 3
    assert len(presidents) == 3


def test_access_by_key():
    yeltsin = presidents["Yeltsin"]
    assert yeltsin["name"] == "Yeltsin"
    assert yeltsin["age"] == 999
    assert yeltsin["country"] == "Russia"


def test_operator_in():
    assert "Yeltsin" in presidents
    assert "Atlas shrugged" not in books


def test_iteration_loops():
    president_list = [president["name"] for president in presidents]
    expected_presidents = ["Yeltsin", "Trump", "Big Man Tyrone"]
    assert president_list == expected_presidents


def test_incorrect_identifier():
    injection = "null; drop table presidents; --"
    with pytest.raises(ValueError, match=f"Table name '{injection}' is incorrect!"):
        TableData(path_to_database, injection)


def test_unexistent_database():
    database_name = "".join(
        (chr(random.randint(97, 122)) for _ in range(10))  # noqa: S311
    )
    database_name = f"{database_name}.sqlite"
    with pytest.raises(
        FileNotFoundError, match=f"Database not found at '{database_name}!"
    ):
        TableData(database_name, "some_table")
