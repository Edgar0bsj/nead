from unittest.mock import MagicMock

import pytest

from src.controller.acessibilidade_controller import (
    AcessibilidadeController,
    AcessibilidadeObject,
)


@pytest.fixture
def acessibilidade():
    return AcessibilidadeController()


def test_show_acess(acessibilidade: AcessibilidadeController):
    resultado = acessibilidade.show_acessibilidade()

    assert isinstance(resultado, list)

    for e in resultado:
        assert isinstance(e, AcessibilidadeObject)


def test_to_manager_export(acessibilidade: AcessibilidadeController):
    acessibilidade.to_manager_export()


def test_show_preview(acessibilidade: AcessibilidadeController):
    acessibilidade.preview()
