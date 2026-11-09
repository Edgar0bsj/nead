import typer

from src.controller.acessibilidade_controller import AcessibilidadeController

acessibilidade_app = typer.Typer(help="Lidando com Acessibilidade")
acess_ctrl = AcessibilidadeController()


@acessibilidade_app.command(name="preview", help="Visualizar os dados")
def preview():
    acess = acess_ctrl.show_acessibilidade()
    print(acess)


@acessibilidade_app.command(name="check", help="Simular e validar o processamento")
def check():
    print("em desenvolvimento")


@acessibilidade_app.command(name="report", help="Consultar o resultado da execução")
def report():
    print("em desenvolvimento")


@acessibilidade_app.command(name="generate", help="gera o CSV definitivo")
def generate():
    print("em desenvolvimento")
