from src.module.base.BaseAnalysis import BaseAnalysis
import pandas as pd

class SaveExcel(BaseAnalysis):
    
    def initialize(self, df:pd.DataFrame, nameFile:str = 'disciplinas_com_multiplos_docentes.xlsx'):
                
        df.to_excel(nameFile,index=False)
        
        return None