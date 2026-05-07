from src.module.base.BaseAnalysis import BaseAnalysis
import pandas as pd


class DealingWithNullValues(BaseAnalysis):
    
    def initialize(self, df:pd.DataFrame):
        df['MATRICULA_PROFESSOR'] = df['MATRICULA_PROFESSOR'].astype(str)
        
        df['MATRICULA_PROFESSOR'] = df['MATRICULA_PROFESSOR'].fillna('SEM PROF')
        df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].fillna('SEM PROF')
        
        return df