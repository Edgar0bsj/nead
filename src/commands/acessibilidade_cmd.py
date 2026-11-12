import typer

acessibilidade_app = typer.Typer(help="Lidando com Acessibilidade")
from src.modules import AcessibilidadeLoad

acess = AcessibilidadeLoad()


@acessibilidade_app.command(
    name="init",
    help="Sobe dados de acessibilidades, Simular e Validar os dados deixando em cache",
)
def init():
    acess.export_tamplate()


@acessibilidade_app.command(name="report", help="Consultar o resultado da execução")
def report():
    print("EM DESENVOLVIMENTO")


@acessibilidade_app.command(name="build", help="gera o CSV definitivo")
def generate():
    print("EM DESENVOLVIMENTO")
