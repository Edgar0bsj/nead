from unittest.mock import MagicMock

import pytest

from src.load.init_load import AcessibilidadeController
from src.model.acessibilidade_model import AcessibilidadeModel


@pytest.fixture
def acessibilidade():
    return AcessibilidadeController()


def test_acess_created(acessibilidade: AcessibilidadeController):
    acess = AcessibilidadeModel(
        name="gegege1", externalId="112122121@321", accessibilityTypeId="T1e2ste2"
    )
    acessibilidade.save(acess)


# def test_acess_update(acessibilidade: AcessibilidadeController):
#     acess = AcessibilidadeModel(
#         name="gegege", externalId="12122121@321", accessibilityTypeId="Te2ste2"
#     )
#     acessibilidade.updated(acess)
