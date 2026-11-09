from rich.console import Console

from src.repository.acessibilidade_repo import AcessibilidadeRepo
from src.service.acessibilidade_service import AcessibilidadeService

console = Console()


class AcessibilidadeController:

    def __init__(self):
        self.repo = AcessibilidadeRepo()
        self.service = AcessibilidadeService()

    def up(self) -> None:
        acess_yaml = self.repo.find_all()
        self.service.validation(acess_yaml)
        self.service.print_up_conclusao(acess_yaml)

        return acess_yaml

    def to_manager_export(self) -> None:
        acess_yaml = self.repo.find_all()
        self.service.validation(acess_yaml)
        df = self.service.create_dataframe(acess_yaml)
        self.service.export_df_to_csv(df)
        self.service.show_sucesso_info(df)
