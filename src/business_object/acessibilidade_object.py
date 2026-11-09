from enum import StrEnum

from pydantic import BaseModel


# =====================================================
#   Acessibilidade Object
# =====================================================
class AcessibilidadeType(StrEnum):
    AUDITORY = "auditory"
    INTELLECTUAL = "intellectual"
    OTHERS = "others"
    PHYSICAL = "physical"
    VISUAL = "visual"


class AcessibilidadeObject(BaseModel):
    nome: str
    externo_id: str
    tipo: AcessibilidadeType
