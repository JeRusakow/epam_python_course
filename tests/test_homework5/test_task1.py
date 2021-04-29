import datetime
from unittest.mock import patch

from pytest import fixture

from homework5.task1.oop_1 import Homework, Student, Teacher


@fixture
def date_01_jan_2020():
    return datetime.datetime(year=2020, month=1, day=1)


@fixture
def date_01_jan_2021():
    return datetime.datetime(year=2021, month=1, day=1)


def test_homework_is_active(date_01_jan_2020, date_01_jan_2021):
    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]

        homework = Homework("Text", 666)
        assert homework.is_active()


def test_homework_is_not_active(date_01_jan_2020, date_01_jan_2021):
    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]
        homework = Homework("Text", 10)
        assert not homework.is_active()


def test_student_do_active_homework(date_01_jan_2020, date_01_jan_2021):
    student = Student("John", "Doe")

    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]
        homework = Homework("Text", 666)

        assert student.do_homework(homework) is homework


def test_student_do_inactive_homework(date_01_jan_2020, date_01_jan_2021):
    student = Student("John", "Doe")

    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]
        homework = Homework("Text", 10)

        assert student.do_homework(homework) is None


def test_teacher_generates_proper_homeworks(date_01_jan_2020):
    hw_text = "Some task"
    days_to_complete = 5
    proper_deadline = datetime.timedelta(days=days_to_complete)

    with patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.return_value = date_01_jan_2020
        homework_from_teacher = Teacher.create_homework(hw_text, days_to_complete)

        assert homework_from_teacher.text == hw_text
        assert homework_from_teacher.created == date_01_jan_2020
        assert homework_from_teacher.deadline == proper_deadline
