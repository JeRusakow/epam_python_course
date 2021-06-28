import datetime
from collections import defaultdict

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeadlineError(Exception):
    """A simple Exception class. To tell a student that they are late."""

    pass


class Human(Base):
    """A common parent class for Teacher and Student.
    Attributes:
        first_name: A Human's first name
        last_name: A Human's last name
    """

    __tablename__ = "humans"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column("first_name", sa.String(60), nullable=False)
    last_name = sa.Column("last_name", sa.String(60), nullable=False)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):
    """A class to represent a student."""

    __tablename__ = "students"
    id = sa.Column("id", sa.Integer, sa.ForeignKey("humans.id"), primary_key=True)
    homework_results = sa.orm.relationship("HomeworkResult", back_populates="author")

    def do_homework(self, homework: "Homework", solution: str) -> "HomeworkResult":
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


class Teacher(Human):
    """A class to represent a students' teacher

    Attributes:
        homework_done (defaultdict): A dictionary storing lists of HomeworkResult
            instances for each Homework. This is a static attribute.
    """

    __tablename__ = "teachers"
    id = sa.Column("id", sa.Integer, sa.ForeignKey("humans.id"), primary_key=True)
    homeworks = sa.orm.relationship("Homework", back_populates="author")

    homework_done = defaultdict(list)

    def create_homework(self, text: str, days_to_complete: int) -> "Homework":
        """Creates a homework instance. Static method.

        Args:
            text: A task's text
            days_to_complete: An amount of days to complete the task

        Returns:
             Homework instance, constructed from above args
        """
        return Homework(text, days_to_complete, self)

    def check_homework(self, done_homework: "HomeworkResult") -> bool:
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


class Homework(Base):
    """
    A class to represent hometasks for students.
    """

    __tablename__ = "homeworks"
    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column("text", sa.String(120), nullable=False)
    deadline = sa.Column("deadline", sa.DateTime, nullable=False)
    solutions = sa.orm.relationship("HomeworkResult", back_populates="task")
    teacher_id = sa.Column(
        "teacher_id", sa.Integer, sa.ForeignKey("teachers.id"), nullable=False
    )
    author = sa.orm.relationship("Teacher", back_populates="homeworks")

    def __init__(self, text: str, days_to_complete: int, author: Teacher):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = self.created + datetime.timedelta(days=days_to_complete)
        self.author = author

    def is_active(self) -> bool:
        """Checks if the time for completing the task is NOT over"""
        return datetime.datetime.now() < self.deadline


class HomeworkResult(Base):
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

    __tablename__ = "homework_results"
    id = sa.Column(sa.Integer, primary_key=True)
    author_id = sa.Column(
        "author_id", sa.Integer, sa.ForeignKey("students.id"), nullable=False
    )
    author = sa.orm.relationship("Student", back_populates="homework_results")
    task_id = sa.Column(
        "task_id", sa.Integer, sa.ForeignKey("homeworks.id"), nullable=False
    )
    task = sa.orm.relationship("Homework", back_populates="solutions")
    solution = sa.Column("solution", sa.String(120), nullable=True)
    created = sa.Column("created", sa.DateTime, nullable=False)

    def __init__(self, author: Student, task: "Homework", solution: str):
        if not isinstance(task, Homework):
            raise TypeError("You gave not a Homework object")

        self.author = author
        self.task = task
        self.solution = solution
        self.created = datetime.datetime.now()
