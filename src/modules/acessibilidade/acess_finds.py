from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from src.modules.acessibilidade.acess_DTO import AcessibilidadeDTO
from src.modules.acessibilidade.acess_model import AcessibilidadeModel


class AcessFinds:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def find_all(
        self,
        name: str | None = None,
        externalId: str | None = None,
        accessibilityTypeId: str | None = None,
    ) -> list[AcessibilidadeDTO]:

        with self.SessionLocal() as session:

            statement = select(AcessibilidadeModel)

            if name:
                statement = statement.where(AcessibilidadeModel.name.ilike(f"%{name}%"))

            if externalId:
                statement = statement.where(
                    AcessibilidadeModel.externalId.ilike(f"%{externalId}%")
                )

            if accessibilityTypeId:
                statement = statement.where(
                    AcessibilidadeModel.externalId.ilike(f"%{accessibilityTypeId}%")
                )

            acess = session.scalars(statement).all()

            buffer = [
                AcessibilidadeDTO(
                    name=e.name,
                    externalId=e.externalId,
                    accessibilityTypeId=e.accessibilityTypeId,
                )
                for e in acess
            ]

            return buffer

    def find_externalId(self, externalId: str) -> AcessibilidadeDTO | None:

        with self.SessionLocal() as session:

            statement = select(AcessibilidadeModel).where(
                AcessibilidadeModel.externalId == externalId
            )
            acess = session.execute(statement).scalar_one_or_none()

            if acess:
                acess = AcessibilidadeDTO(
                    name=acess.name,
                    externalId=acess.externalId,
                    accessibilityTypeId=acess.accessibilityTypeId,
                )

            return acess
