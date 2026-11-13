import typer

from src.handler.command_handler import acess_csv_created, acess_init

app = typer.Typer(
    name="nead",
    help="Ferramenta de automação e integração de dados.",
    epilog="Se funcionou de primeira, não mexe. Não olhe fixamente. Não faça barulho. Apenas aceite o milagre",
)


@app.callback()
def main():
    """Ferramenta de integração de dados."""


@app.command()
def init(acess: bool = typer.Option(False, "--acess", "-ass")):
    if acess:
        acess_init()


@app.command()
def exec(acess: bool = typer.Option(False, "--acess", "-ass")):
    if acess:
        acess_csv_created()


# =============================================
# START
# =============================================
if __name__ == "__main__":
    app()
