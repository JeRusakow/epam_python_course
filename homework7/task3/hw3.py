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
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    # generating array of indices to check
    indices_arr = [tuple(tuple(i, j) for i in range(3)) for j in range(3)]
    indices_arr.append(tuple(tuple(i, i) for i in range(3)))
    indices_arr.append(tuple(tuple(i, 3 - i) for i in range(3)))

    for (x0, y0), (x1, y1), (x2, y2) in indices_arr:
        if board[x0][y0] == board[x1][y1] == board[x2][y2]:
            return f"{board[x0][y0]} wins!"
        if board[y0][x0] == board[y1][x1] == board[y2][x2]:
            return f"{board[y0][x0]} wins!"

    if "-" in [i for j in board for i in j]:
        return "unfinished!"

    return "draw!"
