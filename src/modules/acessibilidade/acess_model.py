from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database import Base


class AcessibilidadeModel(Base):
    __tablename__ = "acessibilidade"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    externalId: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    accessibilityTypeId: Mapped[str] = mapped_column(String(15), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
