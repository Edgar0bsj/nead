from pathlib import Path

import yaml

from src.business_object.acessibilidade_object import AcessibilidadeObject


class AcessibilidadeRepo:
    def find_all(self) -> list[AcessibilidadeObject]:

        base_dir = Path(__file__).resolve().parent.parent.parent
        file_dir = Path("config/acessibilidade.yml")
        file_path = base_dir / file_dir

        with open(file_path, "r", encoding="utf-8") as arquivo:
            content = yaml.safe_load(arquivo)

        acess_dto = [AcessibilidadeObject(**e) for e in content["acessibilidade"]]
        return acess_dto
