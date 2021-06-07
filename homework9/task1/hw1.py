"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Generator, Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:  # noqa: CCR001
    """
    Merges files from list and returns an iterator over sorted sequence. Files must
    contain sorted number sequences divided with newline.

    Args:
        file_list: List of paths to the files

    Returns:
        An iterator over int sequence
    """

    def integer_from_file(file: str) -> Generator[int, None, None]:
        """Creates int generator for the given file"""
        with open(file, "r") as f:
            yield from (int(line) for line in f)
        yield None

    def find_min(numbers: List[Union[int, None]]) -> Union[int, None]:
        """A modified min(), because original min() does not support NoneType"""
        minimum = None

        for num in numbers:
            if minimum is None or (num is not None and num < minimum):
                minimum = num

        return minimum

    num_generators = [integer_from_file(file) for file in file_list]
    integers = [next(gen) for gen in num_generators]

    while (min_num := find_min(integers)) is not None:
        yield min_num
        idx = integers.index(min_num)
        integers[idx] = next(num_generators[idx])

    return
