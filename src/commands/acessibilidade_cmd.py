import typer

acessibilidade_app = typer.Typer(help="Lidando com Acessibilidade")


@acessibilidade_app.command(
    name="up",
    help="Sobe dados de acessibilidades, Simular e Validar os dados deixando em cache",
)
def up():
    print("EM DESENVOLVIMENTO")


@acessibilidade_app.command(name="report", help="Consultar o resultado da execução")
def report():
    print("EM DESENVOLVIMENTO")


@acessibilidade_app.command(name="build", help="gera o CSV definitivo")
def generate():
    print("EM DESENVOLVIMENTO")
