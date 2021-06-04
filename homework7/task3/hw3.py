"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List, Generator, Tuple


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks the tic-tac-toe board for winners

    Args:
        board: a square matrix representing a tic-tac-toe board, filled with 'x', 'o'
            or '-'.

    Returns:
        "x wins!" or "o wins!" if there are winners
        "unfinished!" if there are empty cells
        "draw!" if all the cells are filled but there is no winner
    """
    def win_lines_gen(board_size: int) -> Generator[Tuple[int, int], None, None]:
        """
        A generator of win-lines to check

        Args:
            board_size: the size of a square-shaped board

        Returns: A generator of win-line generators. A win-line generator yields
            tuples of coordinates for a certain win-line
        """

        # horizontal/vertical sweep
        for i in range(board_size):
            yield ((i, j) for j in range(board_size))
            yield ((j, i) for j in range(board_size))

        # main diagonal
        yield ((i, i) for i in range(board_size))
        # side diagonal
        yield ((i, board_size - i - 1) for i in range(board_size))

    for win_line in win_lines_gen(len(board)):
        x_wins = True
        o_wins = True

        for x, y in win_line:
            if board[x][y] != "x":
                x_wins = False
            if board[x][y] != "o":
                o_wins = False

        if x_wins:
            return "x wins!"
        if o_wins:
            return "o wins!"

    if "-" in (i for j in board for i in j):
        return "unfinished!"

    return "draw!"
