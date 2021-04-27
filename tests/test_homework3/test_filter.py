from homework3.task03.task03 import Filter, make_filter


def test_filter_allows_correctly():
    """Tests if the filter allows appropriate items correctly"""
    sample_item = {"name": "me"}

    result = make_filter(name="me").apply([sample_item])

    assert result == [sample_item]


def test_filter_disallows_correctly():
    """Tests if the filter disallows inappropriate items correctly"""
    sample_item = {"name": "me"}

    result = make_filter(name="you").apply([sample_item])

    assert result == []


def test_filter_handle_empty_keys():
    """Tests if the filter is capable to process items with no matching keys"""
    sample_item = {"name": "me"}

    result = make_filter(name="me", age=21).apply([sample_item])

    assert result == []


def test_filter_function_packaging():
    """Filter must be usable with functions passed into constructor as a tuple"""
    f = Filter(lambda a: a > 3, lambda a: a % 2 == 0, lambda a: a < 7)
    result = f.apply([i for i in range(10)])

    assert result == [4, 6]
