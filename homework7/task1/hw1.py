"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Finds the occurrences of element across the given collection.

    Args:
        tree: A collection where the search is performed.  Multiple orders of
            nestedness are supported.
        element: An element to find. Must be of basic type

    Returns:
        The number of occurrences of element across the entire tree.

    Note:
        This function is recursive and may exceed Python recursion limit when run
        against too nested collection.
    """
    if isinstance(tree, dict):
        return sum([find_occurrences(i, element) for i in tree.values()])

    # Element found!
    if tree == element:
        return 1

    # Trying to iterate over 1-symbol strings will cause RecursionError
    if isinstance(tree, str):
        return 0

    # Trying if tree is an iterable
    try:
        return sum([find_occurrences(elem, element) for elem in tree])
    except TypeError:
        return 0


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # noqa  # 6
