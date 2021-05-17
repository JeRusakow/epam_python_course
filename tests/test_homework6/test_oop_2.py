import datetime
import unittest

import pytest

from homework6.task2.oop_2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)


@pytest.fixture()
def date_01_jan_2020():
    return datetime.datetime(year=2020, month=1, day=1)


@pytest.fixture()
def date_01_jan_2021():
    return datetime.datetime(year=2021, month=1, day=1)


@pytest.fixture()
def test_student():
    return Student("John", "Doe")


@pytest.fixture()
def test_homework():
    return Homework("Some task", 10)


def test_homework_is_active(date_01_jan_2020, date_01_jan_2021):
    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]

        homework = Homework("Text", 666)
        assert homework.is_active()


def test_homework_is_not_active(date_01_jan_2020, date_01_jan_2021):
    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]
        homework = Homework("Text", 10)
        assert not homework.is_active()


def test_student_do_active_homework(date_01_jan_2020, date_01_jan_2021):
    student = Student("John", "Doe")

    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [
            date_01_jan_2020,
            date_01_jan_2021,
            date_01_jan_2021,
        ]
        homework = Homework("Text", 666)

        result = student.do_homework(homework, "Some solution")
        assert isinstance(result, HomeworkResult)


def test_student_do_inactive_homework(date_01_jan_2020, date_01_jan_2021):
    student = Student("John", "Doe")

    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.side_effect = [date_01_jan_2020, date_01_jan_2021]
        homework = Homework("Text", 10)

        with pytest.raises(DeadlineError, match="You are late"):
            student.do_homework(homework, "Some solution")


def test_teacher_generates_proper_homeworks(date_01_jan_2020):
    hw_text = "Some task"
    days_to_complete = 5
    proper_deadline = datetime.timedelta(days=days_to_complete)

    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.return_value = date_01_jan_2020
        homework_from_teacher = Teacher.create_homework(hw_text, days_to_complete)

        assert homework_from_teacher.text == hw_text
        assert homework_from_teacher.created == date_01_jan_2020
        assert homework_from_teacher.deadline == proper_deadline


def test_create_homework_result_from_not_a_homework(test_student, date_01_jan_2020):
    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.return_value = date_01_jan_2020

        with pytest.raises(TypeError, match="You gave not a Homework object"):
            HomeworkResult(test_student, "", "Some solution")


def test_check_homework_returns_false_on_poor_homework(test_student):
    teacher = Teacher("John", "Doe")
    hw = Homework("Some task", 10)
    hw_result = HomeworkResult(test_student, hw, "sltn")
    assert not teacher.check_homework(hw_result)


def test_check_homework_returns_true_on_right_homework(test_student, date_01_jan_2020):
    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.return_value = date_01_jan_2020

        teacher = Teacher("John", "Doe")
        hw = Homework("Some task", 10)
        hw_result = HomeworkResult(test_student, hw, "Looong solution")
        assert teacher.check_homework(hw_result)


def test_homeworks_added_to_homework_done(test_student, date_01_jan_2020):
    with unittest.mock.patch("datetime.datetime") as fake_datetime:
        fake_datetime.now.return_value = date_01_jan_2020

        teacher = Teacher("John", "Doe")
        homework_done_size_before = len(teacher.homework_done)
        hw = Homework("Some other task", 10)
        hw_result = HomeworkResult(test_student, hw, "Long solution")
        teacher.check_homework(hw_result)

        homework_done_size_after = len(teacher.homework_done)
        assert homework_done_size_after - homework_done_size_before == 1
        assert hw_result in Teacher.homework_done[hw]
