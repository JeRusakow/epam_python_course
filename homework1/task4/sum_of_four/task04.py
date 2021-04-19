"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Returns the amount of four-numbers tuples across four lists of numbers.
    Straightforwardly tries all possible combinations.
    """
    count = 0
    for elem_a in a:
        for elem_b in b:
            for elem_c in c:
                for elem_d in d:
                    count += int(elem_a + elem_b + elem_c + elem_d == 0)

    return count
