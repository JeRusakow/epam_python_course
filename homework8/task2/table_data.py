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
        cursor = self._conn.cursor()
        cursor.execute(f"select count(*) from {self._table_name}")  # noqa: S608
        return cursor.fetchone()[0]

    def __iter__(self) -> Iterator[sqlite3.Row]:
        cursor = self._conn.execute(f"select * from {self._table_name}")  # noqa: S608
        data = cursor.fetchone()
        while data is not None:
            yield data
            data = cursor.fetchone()

    def __contains__(self, __x: object) -> bool:
        cursor = self._conn.execute(
            f"select * from {self._table_name} where name = ?", (__x,)  # noqa: S608
        )
        data = cursor.fetchone()
        return data is not None

    def __getitem__(self, item: str) -> sqlite3.Row:
        cursor = self._conn.execute(
            f"select from {self._table_name} where name= ?", (item,)  # noqa: S608
        )
        return cursor.fetchone()
