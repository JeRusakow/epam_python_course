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
        with open(file, "r") as file:
            yield from map(int, file)
        yield float("inf")

    gen_list = [integer_from_file(file) for file in file_list]
    # gen_idx is necessary for a case when values from generator are the same
    values_list = [(next(gen), gen_idx) for gen_idx, gen in enumerate(gen_list)]

    heapq.heapify(values_list)

    while values_list[0][0] != float("inf"):
        val, gen_idx = heapq.heappop(values_list)
        heapq.heappush(values_list, (next(gen_list[gen_idx]), gen_idx))
        yield val

    return
