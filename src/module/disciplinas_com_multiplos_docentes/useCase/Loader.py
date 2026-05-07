import pandas as pd

from src.module.base.BaseAnalysis import BaseAnalysis

class Loader(BaseAnalysis):
    
    def initialize(self, nomeFile:str = "C:/Users/unig.ead/Documents/analysis/src/data/sophia.xlsx"):
        df = pd.read_excel(nomeFile)
        
        colunas = [
            'POLO',
            'MODALIDADE',
            'TURMA',
            'DISCIPLINA',
            'NOME_PROFESSOR',
            'MATRICULA_PROFESSOR'
        ]
        
        df = df[colunas]
        return df