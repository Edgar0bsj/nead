from pathlib import Path

from pydantic import ValidationError

from src.modules import AcessibilidadeLoad

acess = AcessibilidadeLoad()


# ============================================
# ACESSIBILIDADE HANDLER
# ============================================
def acess_init():
    acess.export_tamplate()


def acess_csv_created(file_name="acessibilidade.csv"):
    try:
        base_dir = Path().cwd()
        file_path = base_dir / file_name

        result = acess.read_csv(file_path)
        print(result)

    except ValidationError as err:  # noqa: F841
        for erro in err.errors():
            print(erro["loc"])
