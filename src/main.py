import typer

from src.commands.acessibilidade_cmd import acessibilidade_app

app = typer.Typer(
    name="nead",
    help="Ferramenta de automação e integração de dados.",
    epilog="Se funcionou de primeira, não mexe. Não olhe fixamente. Não faça barulho. Apenas aceite o milagre",
)

app.add_typer(acessibilidade_app, name="acess")

# =============================================
# START
# =============================================
if __name__ == "__main__":
    app()
