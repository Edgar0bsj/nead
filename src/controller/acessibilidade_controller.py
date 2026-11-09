from src.repository.acessibilidade_repo import AcessibilidadeObject, AcessibilidadeRepo
from src.service.acessibilidade_service import AcessibilidadeService


class AcessibilidadeController:
    def __init__(self):
        self.repo = AcessibilidadeRepo()
        self.service = AcessibilidadeService()

    def show_acessibilidade(self) -> list[AcessibilidadeObject]:
        return self.repo.find_all()

    def to_manager_export(self) -> None:
        acess_yaml = self.repo.find_all()
        df = self.service.create_dataframe(acess_yaml)
        self.service.export_df_to_csv(df)

    def preview(self) -> None:
        acess_yaml = self.repo.find_all()
        self.service.show_preview(acess_yaml)
