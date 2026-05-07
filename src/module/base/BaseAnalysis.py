from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd


class BaseAnalysis(ABC):
    
    @abstractmethod
    def initialize(self, df:pd.DataFrame)-> Optional[pd.DataFrame]: 
        ...
    
    # METODOS UTEIS
    # def save_to_excel(self, nameFile:str = 'disciplinas_com_multiplos_docentes.xlsx'):
        
    #     if self.df is None: raise ValueError("ATRIBUTO 'df' NÃO PODE SER NONE")
        
    #     self.df.to_excel(nameFile,index=False)
    #     return None
    
    # def get_df(self):
        return self.df