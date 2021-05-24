from homework7.task3.hw3 import tic_tac_toe_checker


def test_x_wins_horizontal():
    brd = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(brd) == "x wins!"


def test_o_wins_vertical():
    brd = [["x", "x", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(brd) == "o wins!"


def test_x_wins_main_diagonal():
    brd = [["x", "o", "o"], ["o", "x", "o"], ["x", "-", "x"]]
    assert tic_tac_toe_checker(brd) == "x wins!"


def test_o_wins_side_diagonal():
    brd = [["x", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(brd) == "o wins!"


def test_unfinished_game():
    brd = [["x", "-", "o"], ["-", "o", "o"], ["-", "x", "x"]]
    assert tic_tac_toe_checker(brd) == "unfinished!"


def test_draw():
    brd = [["o", "x", "o"], ["x", "o", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(brd) == "draw!"
