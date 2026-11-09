from pathlib import Path

import pandas as pd
from rich import box
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.business_object.acessibilidade_object import AcessibilidadeObject

console = Console()


class AcessibilidadeService:
    # ===================================
    def create_dataframe(
        self, acess_object: list[AcessibilidadeObject]
    ) -> pd.DataFrame:
        acess_dict = [ac.model_dump() for ac in acess_object]
        acess_df = pd.DataFrame(acess_dict)
        acess_df = acess_df.rename(
            columns={
                "nome": "name",
                "externo_id": "externalId",
                "tipo": "accessibilityTypeId",
            }
        )
        return acess_df

    # ===================================

    def export_df_to_csv(self, df: pd.DataFrame) -> None:
        out_dir = Path("ava-manager")
        out_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(
            out_dir / "accessibility.unig_producao.csv",
            sep=";",
            encoding="utf-8",
            index=False,
        )

    # ===================================
    def show_preview(self, acess_object: list[AcessibilidadeObject]):
        total = len(acess_object)

        # Tabela de registros
        table = Table(
            title="Registros",
            box=box.ROUNDED,
            header_style="bold cyan",
            border_style="bright_black",
        )

        table.add_column("Nome", style="white")
        table.add_column("Externo ID", style="cyan")
        table.add_column("Tipo", style="magenta")

        for item in acess_object:
            table.add_row(item.nome, item.externo_id, item.tipo)

        # Resumo
        summary = Table.grid(expand=True)
        summary.add_column(justify="center")
        summary.add_column(justify="center")
        summary.add_column(justify="center")

        summary.add_row(
            f"[bold cyan]{total}[/]\n[dim]TOTAL[/]",
            f"[bold green]{total}[/]\n[dim]VÁLIDOS[/]",
            "[bold red]0[/]\n[dim]INVÁLIDOS[/]",
        )

        # Informações
        info = "\n[dim]ORIGEM DOS DADOS:[/] acessibilidade.yml\n[dim]COLUNAS:[/] 3"

        console.print()
        console.print(
            Panel(
                Group(
                    Text("ACESSIBILIDADE", style="bold cyan"),
                    Text("Pré-visualização para exportação", style="dim"),
                    summary,
                    info,
                    table,
                    Text(
                        "Preview concluído. Nenhum arquivo gerado.",
                        style="bold green",
                    ),
                ),
                title="[bold white]NEAD CLI ACESSIBILIDADES[/]",
                subtitle="[cyan]PREVIEW MODE[/]",
                border_style="bright_blue",
                padding=(1, 2),
            )
        )

    # ===================================
    def print_up_conclusao(self, data: list[AcessibilidadeObject]):
        table = Table(
            title="Registros",
            box=box.ROUNDED,
            header_style="bold cyan",
            border_style="bright_black",
        )
        table.add_column("Nome", style="white")
        table.add_column("Externo ID", style="cyan")
        table.add_column("Tipo", style="magenta")

        for item in data:
            table.add_row(item.nome, item.externo_id, item.tipo)

        print("\n")
        console.print(
            Panel(
                Group(
                    f"[bold green]Dados Válidos[/bold green]\n"
                    f"[bold cyan]{len(data)}[/bold cyan] registro analisados",
                    table,
                ),
                title="Status",
                border_style="cyan",
                expand=False,
            ),
        )

    # ===================================
    def validation(self, acess_yaml: list[AcessibilidadeObject]):
        for e in acess_yaml:
            nome = e.nome
            externo_id = e.externo_id
            tipo = e.tipo

            nome_exist = [i for i in acess_yaml if i.nome == nome]
            nome_externo_id = [i for i in acess_yaml if i.externo_id == externo_id]
            nome_tipo = [i for i in acess_yaml if i.tipo == tipo]

            if len(nome_exist) > 1:
                raise ValueError("Nome Duplicado")

            if len(nome_externo_id) > 1:
                raise ValueError("Externo Id Duplicado")

            if len(nome_tipo) > 1:
                raise ValueError("Tipo Duplicado")

    # ===================================
    def show_sucesso_info(self, df: pd.DataFrame):
        summary = Table.grid(expand=True)
        summary.add_column(justify="center")
        summary.add_column(justify="center")

        summary.add_row(
            f"[bold cyan]{len(df)}[/]\n[dim]QUANTIDADE[/]",
            "[bold green]acessibilidade.yml[/]\n[dim]Origin dos dados[/]",
        )

        console.print(
            Panel(
                Group(summary),
                title="Status",
                border_style="cyan",
                expand=False,
            )
        )
