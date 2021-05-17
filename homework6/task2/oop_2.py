"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как-то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаре, сюда попадают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гарантировать отсутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант использования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпляр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """A simple Exception class. To tell a student that they are late."""

    pass


class Human:
    """A common parent class for Teacher and Student.

    Args:
        first_name: A Human's first name
        last_name: A Human's last name

    Attributes:
        first_name: A Human's first name
        last_name: A Human's last name
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """A class to represent hometasks for students.

    Args:
        text: A task itself
        days_to_complete: A term for the task to be completed

    Attributes:
        text (str): A task itself
        deadline (timedelta): A term for the task to be accomplished
        created (datetime): An exact time when the task was created
    """

    def __init__(self, text: str, days_to_complete: int):
        self.text = text
        self.deadline = datetime.timedelta(days=days_to_complete)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Checks if the time for completing the task is NOT over"""
        return datetime.datetime.now() < self.created + self.deadline


class Student(Human):
    """A class to represent a student."""

    def do_homework(self, homework: Homework, solution: str) -> "HomeworkResult":
        """A method to simulate the student's efforts to accomplish the task

        Args:
            homework: The homework to be accomplished
            solution: A solution which the student had come up with

        Returns:
            HomeworkResult instance, if the student is not late, otherwise raises
            an exception

        Raises:
            DeadlineError
        """

        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    """A class to represent the result of student's efforts to accomplish the hometask.

    Args:
        author: A Student instance, who had done the homework
        task: A Homework instance, which had been completed
        solution: A student's solution for task

    Attributes:
        author (Student): A Student instance, who had done the homework
        task (Homework): A Homework instance, which had been completed
        solution (str): A student's solution for task
        created (datetime): An exact time, when the task was solved
    """

    def __init__(self, author: Student, task: Homework, solution: str):
        if not isinstance(task, Homework):
            raise TypeError("You gave not a Homework object")

        self.author = author
        self.task = task
        self.solution = solution
        self.created = datetime.datetime.now()


class Teacher(Human):
    """A class to represent a students' teacher

    Attributes:
        homework_done (defaultdict): A dictionary storing lists of HomeworkResult
            instances for each Homework. This is a static attribute.
    """

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, days_to_complete: int) -> Homework:
        """Creates a homework instance. Static method.

        Args:
            text: A task's text
            days_to_complete: An amount of days to complete the task

        Returns:
             Homework instance, constructed from above args
        """
        return Homework(text, days_to_complete)

    def check_homework(self, done_homework: HomeworkResult) -> bool:
        """Simulates the teacher's efforts to distinguish a properly completed task
        from poorly completed one. If homework completed correctly, puts it into
        collection of all completed homeworks homework_done.

        Args:
            done_homework: A HomeworkResult instance being evaluated

        Returns:
            True if homework completed properly, otherwise False
        """
        if len(done_homework.solution) > 5:
            self.homework_done[done_homework.task].append(done_homework)
            return True

        return False

    @classmethod
    def reset_results(cls, target_homework=None) -> None:
        """Cleans the homework_done collection.
        If target_homework specified, cleans results of this homework. If not,
        clears the entire collection.

        Args:
             target_homework (Homework): A Homework which results are to be cleaned.
                Can be None.
        """
        if target_homework is None:
            cls.homework_done.clear()

        cls.homework_done[target_homework] = []


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")  # noqa
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2  # noqa

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])  # noqa
    print(Teacher.homework_done[docs_hw])  # noqa
    Teacher.reset_results()
