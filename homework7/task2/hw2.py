"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from typing import List


def backspace_compare(first: str, second: str):
    def simulate_text_editor(commands: str) -> List[str]:
        text_on_the_screen = []

        for i in commands:
            if i != "#":
                text_on_the_screen.append(i)
            else:
                try:
                    text_on_the_screen.pop()
                except IndexError:
                    pass

        return text_on_the_screen

    return simulate_text_editor(first) == simulate_text_editor(second)
