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
