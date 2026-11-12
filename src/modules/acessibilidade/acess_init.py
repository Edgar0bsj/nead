from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.database import DATABASE_URL, Base


class AcessInit:
    def __init__(self):
        engine = create_engine(DATABASE_URL, echo=False)
        Base.metadata.create_all(engine)

        self.SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
