from homework7.task1.hw1 import find_occurrences

test_collection_a = {
    "a": None,
    "b": [2, "target", 6, {2: "some_nested", 7: 3, True: 41, "4": "target"}],
    "c": {"n": {"r": "r", "s": "r", "l": [3, 4, 5, "target"]}},
}


def test_nested_dict():
    assert find_occurrences(test_collection_a, "target") == 3
