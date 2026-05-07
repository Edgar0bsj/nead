from src.module.factory.EnumAnalysis import EnumAnalysis
from src.module.disciplinas_com_multiplos_docentes.resource.DisciplinasComMultiplosDocentes import DisciplinasComMultiplosDocentes
from src.module.disciplinas_com_multiplos_docentes.useCase.Loader import Loader
from src.module.disciplinas_com_multiplos_docentes.useCase.FilterByLocationAndModality import FilterByLocationAndModality
from src.module.disciplinas_com_multiplos_docentes.useCase.DealingWithNullValues import DealingWithNullValues
from src.module.disciplinas_com_multiplos_docentes.useCase.QtsProfs import QtsProfs
from src.module.disciplinas_com_multiplos_docentes.useCase.SaveExcel import SaveExcel

class AnalysisToolFactory:
    
    @staticmethod
    def get_class(opcao):
        
        match opcao:
            case EnumAnalysis.DISCIPLINAS_COM_MULTIPLOS_DOCENTES.value:
                
                return DisciplinasComMultiplosDocentes(
                    loader= Loader(),
                    filter_by_location_and_modality=FilterByLocationAndModality(),
                    dealing_with_null_values=DealingWithNullValues(),
                    qts_profs=QtsProfs(),
                    save_excel=SaveExcel()
                )
            
            
            case _:...