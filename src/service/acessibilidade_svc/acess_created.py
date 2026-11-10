from sqlalchemy.orm import Session, sessionmaker

from src.model.acessibilidade_model import AcessibilidadeModel


class AcessCreated:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def save(self, acess_model: AcessibilidadeModel) -> None:

        with self.SessionLocal() as session:

            session.add(acess_model)
            session.commit()

            session.refresh(acess_model)

            return acess_model
