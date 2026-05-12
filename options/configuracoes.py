import questionary


def configuracoes():
    tema = questionary.select(
        "Escolha o tema:",
        choices=["Claro", "Escuro"]
    ).ask()
    print(f"\n Tema definido para: {tema}\n")
    questionary.confirm("Deseja voltar ao menu principal?").ask()