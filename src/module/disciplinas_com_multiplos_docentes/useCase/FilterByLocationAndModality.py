import pandas as pd

from src.module.base.BaseAnalysis import BaseAnalysis

class FilterByLocationAndModality(BaseAnalysis):
    
    def initialize(self, df:pd.DataFrame):
        
        df = df[df['POLO'] == 'Nova Iguaçu']
        df = df[df['MODALIDADE'] == 'G']
        
        df = df[
            ['TURMA', 'DISCIPLINA', 'NOME_PROFESSOR', 'MATRICULA_PROFESSOR']
        ]

        return df