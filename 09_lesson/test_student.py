import pytest

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к БД — укажи свои данные
DATABASE_URL = (
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"
)

# Настройка SQLAlchemy
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


@pytest.fixture(scope="function")
def db_session():
    session = Session()
    trans = session.begin_nested()
    yield session
    trans.rollback()
    session.close()


def test_add_student(db_session):
    new_student = Student(
        user_id=10001,
        level="бакалавр",
        education_form="очная",
        subject_id=1
    )
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(user_id=10001).first()
    assert student is not None
    assert student.level == "бакалавр"


def test_update_student(db_session):
    student = Student(
        user_id=10002,
        level="магистр",
        education_form="заочная",
        subject_id=2
    )
    db_session.add(student)
    db_session.commit()

    student.education_form = "очная"
    db_session.commit()

    updated = db_session.query(Student).filter_by(user_id=10002).first()
    assert updated.education_form == "очная"


def test_delete_student(db_session):
    student = Student(
        user_id=10003,
        level="аспирант",
        education_form="очно-заочная",
        subject_id=3
    )
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(user_id=10003).first()
    assert deleted is None
