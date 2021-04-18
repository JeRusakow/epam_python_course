"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Returns a tuple of maximal and minimal numbers from a """
    min_num = max_num = None

    with open(file_name) as fi:
        for line in fi:
            num = int(line)
            if min_num is None or min_num > num:
                min_num = num
            if max_num is None or max_num < num:
                max_num = num
    return max_num, min_num

