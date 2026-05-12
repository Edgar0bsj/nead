import time

import questionary


def carregar_dados():
    caminho = questionary.text("Digite o caminho do arquivo de dados:").ask()
    print(f"\nCarregando dados de '{caminho}'...")
    time.sleep(2)
    print("✅ Dados carregados com sucesso!\n")
    result = questionary.confirm("Deseja voltar ao menu principal?").ask()
    print(result)