import os
import sqlite3
from contextlib import contextmanager
from typing import Collection, Iterator


class TableData(Collection):
    """
    Wrapper class for a database table.

    Args:
         database_name: a path to database file to connect to
         table_name: a name of the table wrap
    """

    def __init__(self, database_name: str, table_name: str):
        if not os.path.exists(database_name):
            raise FileNotFoundError(f"Database not found at '{database_name}!")

        if not table_name.isidentifier():
            raise ValueError(f"Table name '{table_name}' is incorrect!")

        self.__database_name = database_name
        self.__table_name = table_name

    @contextmanager
    def __open_connection(self) -> sqlite3.Cursor:
        try:
            conn = sqlite3.connect(self.__database_name)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        finally:
            conn.close()

    def __len__(self) -> int:
        with self.__open_connection() as cursor:
            cursor.execute(f"select count(*) from {self.__table_name}")  # noqa: S608
            return cursor.fetchone()[0]

    def __iter__(self) -> Iterator[sqlite3.Row]:
        with self.__open_connection() as cursor:
            yield from cursor.execute(
                f"select * from {self.__table_name}"  # noqa: S608
            )

    def __contains__(self, x: str) -> bool:
        try:
            return self.__getitem__(x) is not None
        except KeyError:
            return False

    def __getitem__(self, item: str) -> sqlite3.Row:
        with self.__open_connection() as cursor:
            cursor.execute(
                f"select * from {self.__table_name} where name= ?",  # noqa: S608
                (item,),
            )
            result = cursor.fetchone()
            if result is None:
                raise KeyError(f"Key '{item}' not found!")
            return result
