"""populated data

Revision ID: f4ea0131b874
Revises: 0b6f951c4b07
Create Date: 2021-06-25 15:56:18.171739

"""

# revision identifiers, used by Alembic.
revision = "f4ea0131b874"
down_revision = "0b6f951c4b07"

from datetime import datetime  # noqa: E402

from alembic import op  # noqa: E402
from models import Homework, HomeworkResult, Human, Student, Teacher  # noqa: E402


def upgrade():
    """Add any optional data upgrade migrations here!"""
    op.bulk_insert(
        Human.__table__,
        [
            {"first_name": "Daniil", "last_name": "Shadrin"},
            {"first_name": "Lev", "last_name": "Sokolov"},
            {"first_name": "Roman", "last_name": "Petrov"},
            {"first_name": "Aleksandr", "last_name": "Smetanin"},
        ],
    )
    op.bulk_insert(Student.__table__, [{"id": 2}, {"id": 3}])
    op.bulk_insert(Teacher.__table__, [{"id": 1}, {"id": 4}])
    op.bulk_insert(
        Homework.__table__,
        [
            {
                "text": "Learn OOP",
                "deadline": datetime.fromisoformat("2021-06-26 15:55:44.968314"),
                "teacher_id": 1,
            },
            {
                "text": "Read docs",
                "deadline": datetime.fromisoformat("2021-06-30 15:55:44.968399"),
                "teacher_id": 1,
            },
        ],
    )
    op.bulk_insert(
        HomeworkResult.__table__,
        [
            {
                "author_id": 2,
                "task_id": 1,
                "solution": "I have done this hw",
                "created": datetime.fromisoformat("2021-06-25 15:55:44.968505"),
            },
            {
                "author_id": 2,
                "task_id": 2,
                "solution": "I have done this hw too",
                "created": datetime.fromisoformat("2021-06-25 15:55:44.968557"),
            },
            {
                "author_id": 3,
                "task_id": 2,
                "solution": "done",
                "created": datetime.fromisoformat("2021-06-25 15:55:44.968605"),
            },
        ],
    )


def downgrade():
    """Add any optional data downgrade migrations here!"""
    op.execute("delete from homework_results")
    op.execute("delete from homeworks")
    op.execute("delete from teachers")
    op.execute("delete from students")
    op.execute("delete from humans")
