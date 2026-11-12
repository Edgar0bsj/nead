from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class AccessibilityType(StrEnum):
    AUDITORY = "auditory"
    INTELLECTUAL = "intellectual"
    OTHERS = "others"
    PHYSICAL = "physical"
    VISUAL = "visual"


name_type = Annotated[str, Field(max_length=50)]
externalId_type = Annotated[str, Field(max_length=50)]


class AcessibilidadeDTO(BaseModel):
    name: name_type
    externalId: externalId_type
    accessibilityTypeId: AccessibilityType

    @field_validator("name", mode="after")
    @classmethod
    def normalizar_name(cls, value: str) -> str:
        return value.strip().lower()

    @field_validator("externalId", mode="after")
    @classmethod
    def normalizar_externalId(cls, value: str) -> str:
        return value.strip().lower()
