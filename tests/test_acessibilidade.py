from unittest.mock import MagicMock

import pytest

from src.controller.acessibilidade_controller import (
    AcessibilidadeController,
)


@pytest.fixture
def acessibilidade():
    return AcessibilidadeController()


def test_show_acess(acessibilidade: AcessibilidadeController):
    acessibilidade.up()
