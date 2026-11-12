from pathlib import Path
from unittest.mock import MagicMock

import pytest

from src.modules import AcessibilidadeLoad


@pytest.fixture
def acessibilidade():
    return AcessibilidadeLoad()


# def test_acess_created(acessibilidade: AcessibilidadeController):
#     path_file = Path(__file__).resolve().parent.parent.parent
#     file_csv = Path("inputs/data.csv")
#     file = path_file / file_csv

#     result = acessibilidade.read_csv(file)

#     [acessibilidade.save(e) for e in result]


def test_acess(acessibilidade: AcessibilidadeLoad):

    result = acessibilidade.export_tamplate()

    print(result)
