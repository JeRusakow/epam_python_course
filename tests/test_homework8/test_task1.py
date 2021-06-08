import random

import pytest

from homework8.task1.key_value_storage import KeyValueStorage


@pytest.fixture(scope="session")
def dummy_storage_path(tmpdir_factory):
    stored_values = {"name": "amen", "numeric_value": 123}

    file_path = tmpdir_factory.mktemp("data").join("dummy_storage.txt")
    with file_path.open("w") as datafile:
        for key, value in stored_values.items():
            datafile.write(f"{key}={value}\n")

    return file_path


@pytest.fixture(scope="session")
def wrong_key_storage_path(tmpdir_factory):
    stored_values = {
        "1ol": "wont work",
    }

    file_path = tmpdir_factory.mktemp("data").join("storage_with_wrong_keys.txt")
    with file_path.open("w") as datafile:
        for key, value in stored_values.items():
            datafile.write(f"{key}={value}\n")

    return file_path


@pytest.fixture(scope="session")
def wrong_key_storage_path_2(tmpdir_factory):
    stored_values = {"n_a;_me": "some name"}
    file_path = tmpdir_factory.mktemp("data").join("storage_with_wrong_keys.txt")
    with file_path.open("w") as datafile:
        for key, value in stored_values.items():
            datafile.write(f"{key}={value}\n")

    return file_path


@pytest.fixture(scope="session")
def non_existent_file():
    random_filename = "".join(
        (chr(random.randint(97, 122)) for _ in range(10))  # noqa: S311
    )
    return f"{random_filename}.txt"


def test_access_by_brackets(dummy_storage_path):
    storage = KeyValueStorage(dummy_storage_path)
    assert storage["name"] == "amen"


def test_access_by_attribute(dummy_storage_path):
    storage = KeyValueStorage(dummy_storage_path)
    assert storage.name == "amen"


def test_integer_type_prevails_over_str(dummy_storage_path):
    storage = KeyValueStorage(dummy_storage_path)
    assert isinstance(storage["numeric_value"], int)


def test_raises_exception_on_unattributable_key(wrong_key_storage_path):
    with pytest.raises(ValueError, match="Key '1ol' cannot be an attribute name!"):
        KeyValueStorage(wrong_key_storage_path)


def test_raises_exception_on_unattributable_key_2(wrong_key_storage_path_2):
    with pytest.raises(ValueError, match="Key 'n_a;_me' cannot be an attribute name!"):
        KeyValueStorage(wrong_key_storage_path_2)


def test_raises_file_does_not_exist_error(non_existent_file):
    with pytest.raises(
        FileNotFoundError, match=f"File '{non_existent_file}' does not exists!"
    ):
        KeyValueStorage(non_existent_file)
