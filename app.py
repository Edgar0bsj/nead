import time
import questionary
from frames.animacao_carregamento import animacao_carregamento
from frames.nead_loading import loading
from colorama import Fore, Style
# opcoes :D
from options.carregar_dados import carregar_dados
from options.analisar_dados import analisar_dados
from options.gerar_relatorio import gerar_relatorio
from options.configuracoes import configuracoes

def menu_principal():
    
    
    loading()
    
    while True:
        escolha = questionary.select(
            "=== MENU PRINCIPAL ===",
            instruction=" ",
            choices=[
                "Carregar dados",
                "Analisar dados",
                "Gerar relatório",
                "Configurações",
                "Sair"
            ]
        ).ask()

        if escolha == "Carregar dados":
            carregar_dados()
        elif escolha == "Analisar dados":
            analisar_dados()
        elif escolha == "Gerar relatório":
            gerar_relatorio()
        elif escolha == "Configurações":
            configuracoes()
        elif escolha == "Sair":
            print("\nSaindo...")
            animacao_carregamento()
            break


if __name__ == "__main__":
    menu_principal()
