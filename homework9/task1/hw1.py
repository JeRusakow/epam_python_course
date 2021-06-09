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
import heapq
from contextlib import ExitStack
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:  # noqa: CCR001
    """
    Merges files from list and returns an iterator over sorted sequence. Files must
    contain sorted number sequences divided with newline.

    Args:
        file_list: List of paths to the files

    Returns:
        An iterator over int sequence
    """
    with ExitStack() as stack:
        sorted_nums = [
            map(int, stack.enter_context(open(file, "r"))) for file in file_list
        ]

        yield from heapq.merge(*sorted_nums, key=int)
