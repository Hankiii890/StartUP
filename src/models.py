from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import String


DATABASE_URL = "postgresql://postgres:1234321@localhost/company"

engine = create_engine(DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


class Defects(Base):
    __tablename__ = "defects"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(55))
    defect: Mapped[str] = mapped_column(String(55))
    title_work: Mapped[str] = mapped_column(String(255))
    unit_of_work: Mapped[str] = mapped_column(String(255))
    headcount: Mapped[int] = mapped_column()


class Employees(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column()  # Telegram
    first_name: Mapped[str] = mapped_column(String(55))
    last_name: Mapped[str] = mapped_column(String(55))
    sheets_sent: Mapped[int] = mapped_column()


# Создание таблиц в БД
Base.metadata.create_all(engine)


# Session для работы с БД
Session = sessionmaker(bind=engine)
session = Session()

