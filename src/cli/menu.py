#python -m src.cli.menu
import questionary
import os

from src.cli.handle.check_professor.check_professor_core import check_professor_core

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(" _   _ _____    _    ____  ")
        print("| \ | | ____|  / \  |  _ \ ")
        print("|  \| |  _|   / _ \ | | | |")
        print("| |\  | |___ / ___ \| |_| |")
        print("|_| \_|_____/_/   \_\____/ ", "\n")

        opcao = questionary.select(
            "========= MENU ==========",
            choices=[
                questionary.Choice("Checar Professores", value="check_professor"),
                questionary.Choice("Sair", value="sair"),
            ],
            pointer=">>>",
            instruction= " "
        ).ask()
        
        match opcao:
            
            case 'check_professor':
                
                check_professor_core(
                    path_data_base= "C:/Users/unig.ead/Documents/analysis/src/data/base.xlsx", 
                    path_data_ref= 'C:/Users/unig.ead/Documents/analysis/src/data/ref.xlsx'
                    )

            case "sair": break

menu()