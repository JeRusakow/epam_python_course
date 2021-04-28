from homework4.task4.task_4_doctest import fizzbuzz


def test_list_size():
    assert len(fizzbuzz(5)) == 5


def test_correctness():
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
    assert fizzbuzz(10) == expected


def test_divisible_by_15():
    result = fizzbuzz(16)
    assert result[14] == "FizzBuzz"
