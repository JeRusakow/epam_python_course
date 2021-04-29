import datetime
from unittest.mock import patch

from homework5.task1.oop_1 import Homework, Student, Teacher


def test_homework_is_active():
    date_of_homework_creation = datetime.datetime(year=2020, month=1, day=1)
    date_of_is_active_check = datetime.datetime(year=2021, month=1, day=1)

    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [
            date_of_homework_creation,
            date_of_is_active_check,
        ]

        homework = Homework("Text", 666)
        assert homework.is_active()


def test_homework_is_not_active():
    date_of_homework_creation = datetime.datetime(year=2020, month=1, day=1)
    date_of_is_active_check = datetime.datetime(year=2021, month=1, day=1)

    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [
            date_of_homework_creation,
            date_of_is_active_check,
        ]

        homework = Homework("Text", 10)
        assert not homework.is_active()
