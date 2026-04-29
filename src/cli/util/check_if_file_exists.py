from pathlib import Path

def check_if_file_exists(caminho:str)-> bool:
    arquivo = Path(caminho)

    if not arquivo.exists() : raise ImportError("O arquivo base.xlsx ou ref.xlsx não se encontra no diretorio \"src/data/\"")

    return True
