from pytest import fixture, raises

from homework4.task1.task_1_read_file import read_magic_number


@fixture(scope="session")
def ok_integer_file_path(tmpdir_factory):
    file_content = "2\nsometext"
    file_path = tmpdir_factory.mktemp("data").join("ok_integer_file.txt")
    with file_path.open("w") as datafile:
        datafile.write(file_content)
    return str(file_path)


@fixture(scope="session")
def ok_float_file_path(tmpdir_factory):
    file_content = "2.78\nsometext"
    file_path = tmpdir_factory.mktemp("data").join("ok_float_file.txt")
    with file_path.open("w") as datafile:
        datafile.write(file_content)
    return str(file_path)


@fixture(scope="session")
def not_ok_integer_file_path(tmpdir_factory):
    file_content = "42\nsometext"
    file_path = tmpdir_factory.mktemp("data").join("not_ok_integer_file.txt")
    with file_path.open("w") as datafile:
        datafile.write(file_content)
    return str(file_path)


@fixture(scope="session")
def not_ok_float_file_path(tmpdir_factory):
    file_content = "-2.78\nsometext"
    file_path = tmpdir_factory.mktemp("data").join("not_ok_float_file.txt")
    with file_path.open("w") as datafile:
        datafile.write(file_content)
    return str(file_path)


@fixture(scope="session")
def without_number_file_path(tmpdir_factory):
    file_content = "aaaaa\nsometext"
    file_path = tmpdir_factory.mktemp("data").join("no_number_file.txt")
    with file_path.open("w") as datafile:
        datafile.write(file_content)
    return str(file_path)


@fixture(scope="session")
def empty_file_path(tmpdir_factory):
    file_path = tmpdir_factory.mktemp("data").join("empty_file.txt")
    with file_path.open("w") as datafile:
        datafile.write("")
    return str(file_path)


@fixture(scope="session")
def file_doesnt_exist_path(tmpdir_factory):
    file_path = tmpdir_factory.mktemp("data").join("empty_file.txt")
    return str(file_path)


@fixture(scope="session")
def not_a_file_path(tmpdir_factory):
    file_path = tmpdir_factory.mktemp("data")
    return str(file_path)


def test_file_with_ok_integer(ok_integer_file_path):
    assert read_magic_number(ok_integer_file_path)


def test_file_with_ok_float(ok_float_file_path):
    assert read_magic_number(ok_float_file_path)


def test_file_with_not_ok_integer(not_ok_integer_file_path):
    assert not read_magic_number(not_ok_integer_file_path)


def test_file_with_not_of_float(not_ok_float_file_path):
    assert not read_magic_number(not_ok_float_file_path)


def test_file_without_number(without_number_file_path):
    with raises(ValueError):
        read_magic_number(without_number_file_path)


def test_empty_file(empty_file_path):
    with raises(ValueError):
        read_magic_number(empty_file_path)


def test_file_doesnt_exits(file_doesnt_exist_path):
    with raises(ValueError):
        read_magic_number(file_doesnt_exist_path)


def test_not_a_file(not_a_file_path):
    with raises(ValueError):
        read_magic_number(not_a_file_path)
