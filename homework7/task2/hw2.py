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
from itertools import zip_longest
from typing import Generator


def backspace_compare(first: str, second: str) -> bool:  # noqa: CCR001
    """
    Compares two strings as if they were printed into text editor.

    Args:
        first: A string which should rather be understood as a command flow.
            Each letter means a key pressed, "#" means backspace.
        second: The same as first

    Returns:
        True, if both command flow cause the same text to appear on the editor,
            false otherwise
    """

    def simulate_text_editor(commands: str) -> Generator[str, None, None]:
        """
        Simulates text editor behaviour

        Args:
            commands: A flow of keys pressed. Consisits of letters and '#' signs.
                '#' sign means 'Backspace' pressed.
        Returns:
            A generator yielding chars in text editor window in reversed order
        """
        chars_to_skip = 0

        for char in reversed(commands):
            if char == "#":
                chars_to_skip += 1
                continue

            if chars_to_skip > 0:
                chars_to_skip -= 1
                continue

            yield char

    for char1, char2 in zip_longest(
        simulate_text_editor(first), simulate_text_editor(second)
    ):
        if char1 != char2:
            return False

    return True
