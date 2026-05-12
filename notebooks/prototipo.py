import numpy as np
import pandas as pd
import unicodedata
from colorama import Fore, Style

from tqdm import tqdm
from .settings import COURSE_MAPPER, PROFESSOR_MAPPER, SETTINGS as CONFIG
from time import sleep
from thefuzz import process

def get_dataFrame()-> pd.DataFrame:
    df = pd.read_excel(CONFIG['analise-base-xlsx'])
    return df
    
def apply_filters(df: pd.DataFrame)-> pd.DataFrame:
    
    for coluna, valor in CONFIG["filtros"].items():
        df = df[df[coluna] == valor]
    
    df["ENTRADA"] = df["TURMA"].str.extract(r'\.(\d)\.\dP\s-')
    df = df[ df['ENTRADA'] == CONFIG["entrada"] ]
    
    return df

def add_new_columns(df: pd.DataFrame)-> pd.DataFrame:
    
    df["CURSO"] = df['TURMA'].str.extract(r'^[^-]*-[^-]*-(.*)')
    df['PERIODO'] = df['TURMA'].str.extract(r'(\d)P\s-')
    
    
    return df
def select_interest_columns(df: pd.DataFrame)-> pd.DataFrame:
    
    df = df[['TURMA', 'DISCIPLINA', 'NOME_PROFESSOR', 'CURSO', 'PERIODO']]
    
    return df

def remove_duplicates_with_offset(df: pd.DataFrame)-> pd.DataFrame:
    
    df = df.drop_duplicates(subset=['TURMA', 'DISCIPLINA', 'NOME_PROFESSOR', 'CURSO', 'PERIODO'])
    
    return df

def remove_null(df: pd.DataFrame)-> pd.DataFrame:
    df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].fillna("vazio")
    return df

def normalize_period_column(df: pd.DataFrame)-> pd.DataFrame:
    df['PERIODO'] = df['PERIODO'].fillna(0)
    df['PERIODO'] = df['PERIODO'].astype(int)
    return df
    

def replace_values_mapper(df: pd.DataFrame)-> pd.DataFrame:
    
    df['CURSO'] = df['CURSO'].str.title()
    df['CURSO'] = df['CURSO'].str.strip()
    df['CURSO'] = df['CURSO'].replace(COURSE_MAPPER)
    
    df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].str.title()
    df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].str.strip()
    df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].replace(PROFESSOR_MAPPER)

    
    return df

import pandas as pd
from time import sleep

def mech_data(df: pd.DataFrame, dff_path: str, threshold: int = 90) -> pd.DataFrame:
    dff = pd.read_excel(dff_path)

    cursos_ref = dff['CURSO'].dropna().unique().tolist()
    periodos_ref = dff['PERÍODO'].dropna().unique().tolist()
    disciplinas_ref = dff['DISCIPLINA'].dropna().unique().tolist()
    professores_ref = dff['PROFESSORES'].dropna().unique().tolist()

    status = []

    for _, row in tqdm(df.iterrows(),total=len(df), colour='cyan'):
        curso = row['CURSO']
        disciplina = row['DISCIPLINA']
        periodo = row['PERIODO']
        professor = row['NOME_PROFESSOR']

        curso_match, curso_score = process.extractOne(str(curso), cursos_ref)
        disciplina_match, disciplina_score = process.extractOne(str(disciplina), disciplinas_ref)
        periodo_match, periodo_score = process.extractOne(str(periodo), periodos_ref)
        professor_match, professor_score = process.extractOne(str(professor), professores_ref)

        curso_check = curso_score >= threshold
        disciplina_check = disciplina_score >= threshold
        periodo_check = periodo_score >= threshold
        professor_check = professor_score >= threshold

        if curso_check and disciplina_check and periodo_check and professor_check:
            msg = "OK"
        elif not any([curso_check, disciplina_check, periodo_check, professor_check]):
            msg = "Nenhum dado foi compatível"
        elif not curso_check:
            msg = f"Falhou em achar o curso (mais próximo: {curso_match}, score={curso_score})"
        elif not disciplina_check:
            msg = f"Falhou em achar a disciplina (mais próximo: {disciplina_match}, score={disciplina_score})"
        elif not periodo_check:
            msg = f"Falhou em achar o período (mais próximo: {periodo_match}, score={periodo_score})"
        elif not professor_check:
            msg = f"Falhou em achar o professor (mais próximo: {professor_match}, score={professor_score})"
        else:
            msg = "Erro não mapeado"

        # print(msg)
        tqdm.write(Fore.YELLOW + f"[process] {msg} CURSO: {curso} DISCIPLINA: {disciplina} PERIODO: {periodo} PROFESSOR: {professor} " + Style.RESET_ALL)
        status.append(msg)
        sleep(0.03)

    df['STATUS'] = status
    return df

# =============
df = get_dataFrame()
df = apply_filters(df)
df = add_new_columns(df)
df = remove_null(df)
df = normalize_period_column(df)
df = select_interest_columns(df)
df = remove_duplicates_with_offset(df)
df = replace_values_mapper(df)
df = mech_data(df, 'C:/Users/unig.ead/Documents/analysis/data/mapa-referencia-xlsx.xlsx')

print(df.head())
print(df.info())

# df.to_excel("resultado.xlsx", index= False)

