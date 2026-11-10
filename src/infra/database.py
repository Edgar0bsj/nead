from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///src/infra/database.db"


class Base(DeclarativeBase):
    pass
