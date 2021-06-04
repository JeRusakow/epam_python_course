import os
import re


class KeyValueStorage:
    """
    Class-wrapper for dict-like storage structure.
    A value can be got by 'instance[key]' or 'instance.key'.
    If value can be treated both as a str and an int, int is preferred.

    Args:
        filename: A storage file with following structure:

            key1=val1
            key2=val2

    Raises:
        ValueError: if 'key' is an inappropriate name to be an attribute
    """

    def __init__(self, filename: str):  # noqa: CCR001
        self.__storage = {}

        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' does not exists!")

        with open(filename) as file:
            for line in file:
                splitted = line.rstrip("\n").split(sep="=", maxsplit=1)

                if re.match(r"^_*[a-zA-Z]+[a-zA-Z0-9_]*$", splitted[0]):
                    try:
                        self.__storage[splitted[0]] = int(splitted[1])
                    except ValueError:
                        self.__storage[splitted[0]] = splitted[1]
                else:
                    raise ValueError(
                        f"Key '{splitted[0]}' cannot be an attribute name!"
                    )

    def __getitem__(self, item):
        return self.__storage[item]

    def __getattr__(self, item):
        try:
            return self.__storage[item]
        except KeyError:
            raise AttributeError


class Some:
    pass
