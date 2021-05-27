from homework8.task2.table_data import TableData

presidents = TableData("example.sqlite", "presidents")
books = TableData("example.sqlite", "books")


def test_len():
    assert len(presidents) == 3
    assert len(books) == 3


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
