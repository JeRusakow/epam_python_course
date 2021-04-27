from homework4.task4.task_4_doctest import fizzbuzz


def test_list_size():
    assert len(fizzbuzz(5)) == 5


def test_correctness():
    expected = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]
    assert fizzbuzz(10) == expected
