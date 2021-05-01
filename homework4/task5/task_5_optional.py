"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(6))
["1", "2", "Fizz", "4", "Buzz", "Fizz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import Generator, List


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """Generates a Fizz-Buzz sequence fo length n. Does not use itertools.cycle"""
    fizzes = ["Fizz", "", ""]
    buzzes = ["Buzz", "", "", "", ""]

    for elem in [(fizzes[i % 3] + buzzes[i % 5]) or str(i) for i in range(1, n + 1)]:
        yield elem
