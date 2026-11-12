import pandas as pd

from src.modules.acessibilidade.acess_DTO import AcessibilidadeDTO


class AcessReadCsv:
    def __init__(self):
        pass

    def read_csv(self, path_file) -> list[AcessibilidadeDTO]:

        acess_list = pd.read_csv(path_file, sep=";", encoding="utf-8").to_dict(
            "records"
        )

        acess_buffer = [AcessibilidadeDTO(**e) for e in acess_list]

        return acess_buffer
