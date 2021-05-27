import sqlite3
from typing import Collection, Iterator


class TableData(Collection):
    """
    Wrapper class for a database table.

    Args:
         database_name: a path to database file to connect to
         table_name: a name of the table wrap
    """

    def __init__(self, database_name: str, table_name: str):
        self._conn = sqlite3.connect(database_name)
        self._conn.row_factory = sqlite3.Row
        self._table_name = table_name

    def __len__(self) -> int:
        cursor = self._conn.execute("select count(*) from ?", (self._table_name,))
        return cursor.fetchone()[0]

    def __iter__(self) -> Iterator[sqlite3.Row]:
        cursor = self._conn.execute("select * from ?", (self._table_name,))
        data = cursor.fetchone()
        while data is not None:
            yield data
            data = cursor.fetchone()

    def __contains__(self, __x: object) -> bool:
        cursor = self._conn.execute(
            "select * from ? {} where name=?", (self._table_name, __x)
        )
        data = cursor.fetchone()
        return data is not None

    def __getitem__(self, item: str) -> sqlite3.Row:
        cursor = self._conn.execute(
            "select * from ? where name=?", (self._table_name, item)
        )
        return cursor.fetchone()
