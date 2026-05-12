import time

import questionary


def gerar_relatorio():
    formato = questionary.select(
        "Escolha o formato do relatório:",
        choices=["txt", "csv", "json"]
    ).ask()
    print(f"\n Gerando relatório em formato {formato}...")
    time.sleep(2)
    print(" Relatório gerado com sucesso!\n")
    questionary.confirm("Deseja voltar ao menu principal?").ask()