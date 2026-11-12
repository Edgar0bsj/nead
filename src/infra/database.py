from pathlib import Path

from sqlalchemy.orm import DeclarativeBase

base_dir = Path(__file__).resolve().parent

DATABASE_URL = f"sqlite:///{base_dir/"database.db"}"


class Base(DeclarativeBase):
    pass
