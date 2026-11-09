import typer

from src.controller.acessibilidade_controller import AcessibilidadeController

acessibilidade_app = typer.Typer(help="Lidando com Acessibilidade")
acess_ctrl = AcessibilidadeController()


@acessibilidade_app.command(
    name="up",
    help="Sobe dados de acessibilidades, Simular e Validar os dados deixando em cache",
)
def up():
    try:
        acess_ctrl.up()
    except Exception as err:
        print(err)


@acessibilidade_app.command(name="report", help="Consultar o resultado da execução")
def report():
    acess_ctrl.report()


@acessibilidade_app.command(name="build", help="gera o CSV definitivo")
def generate():
    acess_ctrl.to_manager_export()
