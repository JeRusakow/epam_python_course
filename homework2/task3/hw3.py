"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so on.

You may assume that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Returns a List of all possible combinations of elements where the first element is from the first given list,
    the second element is from the second one and so on.
    """
    result = [[]]

    for list in args:
        result = [subresult + [elem] for subresult in result for elem in list]

    return result
