import csv

from base import Session, engine
from models import Homework, HomeworkResult, Student, Teacher


def get_report():
    reports = []

    with Session(bind=engine) as session:
        query = (
            session.query(HomeworkResult, Homework, Student, Teacher)
            .join(Homework, Homework.id == HomeworkResult.task_id)
            .join(Teacher, Teacher.id == Homework.teacher_id)
            .join(Student, Student.id == HomeworkResult.author_id)
            .all()
        )

        for _, hw, stu, tch in query:
            hw_report = {
                "student_name": f"{stu.first_name} {stu.last_name}",
                "teacher_name": f"{tch.first_name} {tch.last_name}",
                "homework_deadline": str(hw.deadline),
            }
            reports.append(hw_report)
    with open("report.csv", "w") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["student_name", "teacher_name", "homework_deadline"]
        )
        writer.writeheader()
        writer.writerows(reports)


if __name__ == "__main__":
    get_report()
