import re
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
        if not re.match(r"^[_a-zA-Z]+[_a-zA-Z09]$", table_name):
            raise ValueError(f"Table name '{table_name}' is incorrect!")

        self.__database_name = database_name
        self.__table_name = table_name

    def __open_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.__database_name)
        conn.row_factory = sqlite3.Row
        return conn

    def __len__(self) -> int:
        with self.__open_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"select count(*) from {self.__table_name}")  # noqa: S608
            return cursor.fetchone()[0]

    def __iter__(self) -> Iterator[sqlite3.Row]:
        with self.__open_connection() as conn:
            cursor = conn.execute(f"select * from {self.__table_name}")  # noqa: S608

        while (data := cursor.fetchone()) is not None:
            yield data

    def __contains__(self, x: str) -> bool:
        return self.__getitem__(x) is not None

    def __getitem__(self, item: str) -> sqlite3.Row:
        with self.__open_connection() as conn:
            cursor = conn.execute(
                f"select * from {self.__table_name} where name= ?",  # noqa: S608
                (item,),  # noqa: S608
            )
            return cursor.fetchone()
