"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checks if the sequence is a Fibonacci sequence"""
    if len(data) < 2:
        return False

    rev_iter = reversed(data)

    a = next(rev_iter)
    b = next(rev_iter)

    for item in rev_iter:
        # print(f"debug {item}")
        c = a - b
        try:
            if c != item:
                return False
            a = b
            b = c
        except StopIteration:
            break

    while a >= 0 and b >= 0:
        # print(f"a = {a}, b = {b}, c = {c}")

        c = a - b

        if b == 0 and a == 1:
            return True

        a = b
        b = c

    return False


def main():
    data = [1, 1, 2, 3, 5, 8, 13, 21]

    print(check_fibonacci(data))


if __name__ == "__main__":
    main()
