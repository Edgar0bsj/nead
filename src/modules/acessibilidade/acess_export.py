from pathlib import Path

import pandas as pd


class AcessExport:
    def __init__(self):
        pass

    def export_tamplate(self):
        dir_atual = Path().cwd()
        file_name = "acessibilidade.csv"

        tamplate = {}

        tamplate["name"] = [""]
        tamplate["externalId"] = [""]
        tamplate["accessibilityTypeId"] = [""]

        pd.DataFrame(tamplate).to_csv(
            dir_atual / file_name, sep=";", encoding="utf-8", index=False
        )
