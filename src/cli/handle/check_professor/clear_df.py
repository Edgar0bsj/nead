import pandas as pd
def clear_data(df_base:pd.DataFrame, df_ref:pd.DataFrame , entrada:int)-> list[pd.DataFrame]:
    # Base dataframe =======================================================
    cols_base = ["POLO","MODALIDADE","TURMA","DISCIPLINA","NOME_PROFESSOR"]
    filtro_polo = "Nova Iguaçu"
    filtro_modalidade = "G"
    cols_export = ["TURMA","DISCIPLINA","NOME_PROFESSOR"]

    df_base = df_base[cols_base]
    df_base = df_base[df_base["POLO"] == filtro_polo]
    df_base = df_base[df_base["MODALIDADE"] == filtro_modalidade]
    df_base = df_base[df_base['TURMA'].str.contains(rf'\.{entrada}\.\dP', regex=True)]

    df_base = df_base[cols_export]

    # Reference dataframe =======================================================
    cols_ref = ["CURSO","PERÍODO","DISCIPLINA","PROFESSORES"]

    df_ref = df_ref[cols_ref]


    return [df_base, df_ref]




