import pandas as pd
from typing import Optional


class Mdi:
    def __init__(self):
        self.df:Optional[pd.DataFrame] = None
        
        self.init()
    
    def init(self):
        df = self.loader()
        df = self.filter_by_location_and_modality(df)
        df = self.dealing_with_null_values(df)
        df = self.qts_profs(df)
        
        self.df = df
        
        return self
    
    def loader(self):
        df = pd.read_excel("C:/Users/unig.ead/Documents/analysis/src/data/dados_atualizado.xlsx")
        
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

    def filter_by_location_and_modality(self, df:pd.DataFrame):
        
        df = df[df['POLO'] == 'Nova Iguaçu']
        df = df[df['MODALIDADE'] == 'G']
        
        df = df[
            ['TURMA', 'DISCIPLINA', 'NOME_PROFESSOR', 'MATRICULA_PROFESSOR']
        ]

        return df
    
    def dealing_with_null_values(self, df:pd.DataFrame):
        
        df['MATRICULA_PROFESSOR'] = df['MATRICULA_PROFESSOR'].astype(str)
        
        df['MATRICULA_PROFESSOR'] = df['MATRICULA_PROFESSOR'].fillna('SEM PROF')
        df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].fillna('SEM PROF')
        
        return df
    
    def qts_profs(self, df:pd.DataFrame):
        
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
    
    def save_to_excel(self):
        
        if self.df is None: raise ValueError("ATRIBUTO 'df' NÃO PODE SER NONE")
        
        self.df.to_excel("disciplinas_com_multiplos_docentes.xlsx",index=False)
        return None
    
    def getDf(self):
        return self.df