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
        self._storage = {}

        with open(filename) as file:
            for line in file:
                splitted = line.rstrip("\n").split(sep="=", maxsplit=1)
                try:
                    self._storage[splitted[0]] = int(splitted[1])
                except ValueError:
                    self._storage[splitted[0]] = splitted[1]

        for key, value in self._storage.items():
            if not re.match(r"_*[a-zA-Z]+[a-zA-Z0-9_]*", key):
                raise ValueError(f"Key '{key}' cannot be an attribute name!")
            if key not in self.__dict__:
                self.__setattr__(key, value)

    def __getitem__(self, item):
        return self._storage[item]
