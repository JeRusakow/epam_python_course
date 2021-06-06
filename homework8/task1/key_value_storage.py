import os
from keyword import iskeyword


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

                if splitted[0].isidentifier() and not iskeyword(splitted[0]):
                    if splitted[1].isnumeric():
                        self.__storage[splitted[0]] = int(splitted[1])
                    else:
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
