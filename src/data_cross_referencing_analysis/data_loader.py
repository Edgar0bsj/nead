import pandas as pd


def loaderData():
    df = pd.read_excel("C:/Users/unig.ead/Documents/analysis/src/data/dados_atualizado.xlsx")
    dff = pd.read_excel("C:/Users/unig.ead/Documents/analysis/src/data/ref.xlsx")
    
    df = df[["POLO",'TURMA',"DISCIPLINA","NOME_PROFESSOR","MODALIDADE"]]
    
    dff = dff[['CURSO','PERÍODO','DISCIPLINA','PROFESSORES']]
    
    return [df, dff]
