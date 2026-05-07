import pandas as pd
from rapidfuzz import process

from src.data_cross_referencing_analysis.mapping.course_mapping import COURSE_MAPPER
from src.data_cross_referencing_analysis.mapping.teacher_mapping import TEACHER_MAPPING

def corrigir(valor, lista_referencia):
    match, score, _ = process.extractOne(valor, lista_referencia)

    if score > 80:
        return match
    return valor

def limpar_texto(col):
    return (
        col
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)  # remove espaços duplicados
        .str.replace(r"[\n\t\r]", "", regex=True)  # remove quebras invisíveis
    )


def cleaningData(df:pd.DataFrame, dff:pd.DataFrame):
    
    df = df[ (df['POLO'] == "Nova Iguaçu") & (df['MODALIDADE'] == "G") ]
    
    df["_CURSO"] = df['TURMA'].str.extract(r'^[^-]*-[^-]*-(.*)')
    df['_PERIODO'] = df['TURMA'].str.extract(r'(\d)P\s-')
    df["_ENTRADA"] = df["TURMA"].str.extract(r'\.(\d)\.\dP\s-')
    
    df = df[ df['_ENTRADA'] == "2" ]
    
    df['DISCIPLINA'] = df["DISCIPLINA"].str.lower()
    df['NOME_PROFESSOR'] = df["NOME_PROFESSOR"].str.lower()
    df['_CURSO'] = df["_CURSO"].str.lower()
    
    df = df[['_CURSO',"_PERIODO","DISCIPLINA","NOME_PROFESSOR","TURMA"]]
    
    df["_CURSO"] = df["_CURSO"].replace(COURSE_MAPPER)
    df["NOME_PROFESSOR"] = df["NOME_PROFESSOR"].replace(TEACHER_MAPPING)
    df['_PERIODO'] = df['_PERIODO'].fillna(0)
    df['_PERIODO'] = df['_PERIODO'].astype(int)
    
    df = df.rename(columns={'_CURSO': 'CURSO', '_PERIODO': 'PERIODO'})
    
    df = df.drop_duplicates(subset=["CURSO", "PERIODO","NOME_PROFESSOR","DISCIPLINA"])
    
    df['DISCIPLINA'] = df['DISCIPLINA'].astype(str).str.strip().str.lower()
    df['DISCIPLINA'] = limpar_texto(df['DISCIPLINA'])
    
    df['NOME_PROFESSOR'] = limpar_texto(df['NOME_PROFESSOR'])
    df['NOME_PROFESSOR'] = df['NOME_PROFESSOR'].astype(str).str.strip().str.lower()
    
    df = df.rename(columns={'DISCIPLINA': 'DISCIPLINA_SOPHIA'})
    
    # =============== DFF
    
    dff = dff.rename(columns={'PERÍODO': 'PERIODO', 'PROFESSORES': 'NOME_PROFESSOR'})
    dff['DISCIPLINA'] = dff['DISCIPLINA'].astype(str).str.strip().str.lower()

    dff['DISCIPLINA'] = limpar_texto(dff['DISCIPLINA'])
    dff['NOME_PROFESSOR'] = limpar_texto(dff['NOME_PROFESSOR'])
    dff['NOME_PROFESSOR'] = dff['NOME_PROFESSOR'].astype(str).str.strip().str.lower()

    dff = dff.rename(columns={'DISCIPLINA': 'DISCIPLINA_PLANILHA'})

    return [df, dff]

