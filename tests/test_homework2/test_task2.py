from homework2.task2.hw2 import major_and_minor_elem


def test_major_and_minor_elem():
    """Checks if the function works properly"""
    test_data = [1, 1, 2, 2, 1, 1]

    assert major_and_minor_elem(test_data) == (1, 2)
