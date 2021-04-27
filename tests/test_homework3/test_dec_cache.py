from unittest.mock import Mock

from homework3.task01.dec_cache import dec_cached


def test_original_and_cached_return_the_same():
    """Tests if original and decorated function return the same"""

    @dec_cached(times=1)
    def sample_func(x):
        return x

    assert sample_func(10) == 10


def test_function_result_reuse():
    """Tests if the decorator reuses function output and not calls the function"""
    mock_func = Mock()
    mock_func.return_value = 10

    @dec_cached(times=2)
    def sample_func(x):
        return mock_func(x)

    _ = sample_func(None)
    _ = sample_func(None)

    mock_func.assert_called_once()


def test_times_parameter():
    """Tests 'times' parameter. The original function must be called again
    once per each several cached function calls"""
    mock_func = Mock()
    mock_func.return_value = 10

    @dec_cached(times=2)
    def sample_func(x):
        return mock_func(x)

    _ = sample_func(None)
    _ = sample_func(None)
    _ = sample_func(None)

    assert mock_func.call_count == 2
