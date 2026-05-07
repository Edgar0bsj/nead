from src.module.base.BaseAnalysis import BaseAnalysis


class DisciplinasComMultiplosDocentes():
    def __init__(self,
                 loader:BaseAnalysis,
                 filter_by_location_and_modality:BaseAnalysis,
                 dealing_with_null_values:BaseAnalysis,
                 qts_profs:BaseAnalysis,
                 save_excel:BaseAnalysis,
                 ):
        
        self.loader = loader
        self.filter_by_location_and_modality = filter_by_location_and_modality
        self.dealing_with_null_values = dealing_with_null_values
        self.qts_profs = qts_profs
        self.save_excel = save_excel

    def GerarPlanilhaDisciplinasMultidocentes(self)-> bool:
        try:

            df = self.loader.initialize()
            df = self.filter_by_location_and_modality.initialize(df)
            df = self.dealing_with_null_values.initialize(df)
            df = self.qts_profs.initialize(df)
            df = self.save_excel.initialize(df)
        
            return True
        
        except Exception as err:
            
            print('classe: DisciplinasComMultiplosDocentes')
            print('metodo: "GerarPlanilhaDisciplinasMultidocentes"')
            print(err)
            
            return False