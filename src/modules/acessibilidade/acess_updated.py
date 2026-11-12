from sqlalchemy.orm import Session, sessionmaker

from src.modules.acessibilidade.acess_DTO import AcessibilidadeDTO
from src.modules.acessibilidade.acess_model import AcessibilidadeModel


class AcessUpdated:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def updated(self, id: str, acess_dto: AcessibilidadeDTO) -> None:

        with self.SessionLocal() as session:
            acess = session.get(AcessibilidadeModel, id)

            acess.name = acess_dto.name
            acess.externalId = acess_dto.externalId
            acess.accessibilityTypeId = acess_dto.accessibilityTypeId

            session.commit()
            session.refresh(acess)

            return acess
