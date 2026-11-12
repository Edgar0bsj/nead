from sqlalchemy.orm import Session, sessionmaker

from src.modules.acessibilidade.acess_DTO import AcessibilidadeDTO
from src.modules.acessibilidade.acess_model import AcessibilidadeModel


class AcessCreated:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def save(self, acess_dto: AcessibilidadeDTO) -> None:

        acess_dto = acess_dto.model_dump()
        model = AcessibilidadeModel(**acess_dto)

        with self.SessionLocal() as session:

            session.add(model)
            session.commit()

            session.refresh(model)

            return model
