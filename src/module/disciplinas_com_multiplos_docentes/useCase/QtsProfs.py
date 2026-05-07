from src.module.base.BaseAnalysis import BaseAnalysis
import pandas as pd


class QtsProfs(BaseAnalysis):
    
    
    def initialize(self, df:pd.DataFrame): 
        resultado = (
            df.groupby("DISCIPLINA")["NOME_PROFESSOR"]
            .nunique()
            .reset_index(name="qtd_prof")
        )
        
        resultado = resultado.merge(
            df[["DISCIPLINA", "TURMA", "NOME_PROFESSOR", "MATRICULA_PROFESSOR"]].drop_duplicates(),
            on="DISCIPLINA",
            how="left"
        )
        
        resultadoFiltro = resultado[
            resultado["qtd_prof"] > 1
        ]
        
        return resultadoFiltro
    