from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from src.modules.acessibilidade.acess_model import AcessibilidadeModel


class AcessDeleted:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def deleted(self, id: int) -> bool:

        with self.SessionLocal() as session:

            entity = session.get(AcessibilidadeModel, id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True

    def deleted_to_externoId(self, externalId: str) -> bool:

        with self.SessionLocal() as session:

            statement = select(AcessibilidadeModel).where(
                AcessibilidadeModel.externalId == externalId
            )

            acess = session.execute(statement).scalar_one_or_none()

            if not acess:
                return False

            entity = session.get(AcessibilidadeModel, acess.id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True
