from homework4.task5.task_5_optional import fizzbuzz


def test_generator_duration():
    result = list(fizzbuzz(5))
    assert len(result) == 5


def test_generator_result():
    result = list(fizzbuzz(6))
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz"]


def test_divisible_by_both_3_and_5():
    result = list(fizzbuzz(16))
    assert result[14] == "FizzBuzz"
