"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Returns a tuple of the most and the least common elements from given array"""
    elements_counter = {}

    for elem in inp:
        if elem not in elements_counter.keys():
            elements_counter[elem] = 1
        else:
            elements_counter[elem] += 1

    elements_counter = sorted(elements_counter.items(), key=lambda x: x[1])

    # Since the presence of the most common element is guaranteed, further checks are redundant

    return elements_counter[-1][0], elements_counter[0][0]
