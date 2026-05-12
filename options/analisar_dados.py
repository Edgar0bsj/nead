import time

import questionary


def analisar_dados():
    tipo = questionary.select(
        "Escolha o tipo de análise:",
        choices=[
            "Quantas disciplina tem mais de um professor",
            "Cruzar dados com a entrada de professores (EAD)",
            "Correlação"
        ]
    ).ask()
    print(f"\n Processando análise: {tipo}...")
    time.sleep(2)
    print(f" Resultado da análise ({tipo}): Exemplo de saída simulada.\n")
    questionary.confirm("Deseja voltar ao menu principal?").ask()