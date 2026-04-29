import pandas as pd
from thefuzz import fuzz
from tqdm import tqdm

from src.cli.util.text_cleaning import text_cleaning

def check_courses(df_base:pd.DataFrame, df_ref:pd.DataFrame)-> pd.DataFrame:
    status_check = []
    abbreviations = {
        "SERV SOC":"Serviço Social",
        "GEST TI":"Gestão da Tec. da Informaçã",
        "LOGIST":"Logistica",
        "ED FI LIC":"Educação Física Bacharelado",
        "PEDAG":"Pedagogia",
        "SEG PUBL":"Segurança Pública",
        "ENG ELET":"Engenharia Elétrica",
        "GEST FINAN":"Gestão Financeira",
        "ADM":"Administração",
        "BIOM":"Biomedicina",
        "CIE COMP":"Ciencia da Computacao",
        "MARKET":"Marketing",
        "ED FI BACH":"Educação Fisica",
        "ED FI LIC":"Educacao Fisica",
        "REC HUM":"Gestao de Recursos Humanos",
        "GEST AMB":"Gestao Ambiental",
        "C CONTAB":"Ciencias Contábeis",
        "ADS":"Análise e Des de Sistemas",
        "GEST PUBL":"Gestao Publica",
        "redescom":"Redes de Computadores",
        "COMEX":"Comercio Exterior",
        "PROC GER":"Processos Gerenciais",
        "ENG PROD":"Engenharia de Produção",
        "ENG PROD":"Engenharia de Producao",
        "MATEM":"Matemática",
        }

    for turma in tqdm(
        iterable= zip(df_base['TURMA']),
        desc='VERIFICANDO CURSOS...',
        total= len(df_base),
        unit= "MB"
    ):
        partes = str(turma).split("-")

        if len(partes) >= 3:
            curso_alvo = text_cleaning(partes[2].strip()) 
        else:
            curso_alvo = ""

        encontrou = False

        for curso_ref in df_ref['CURSO']:
            curso_ref_limpo = text_cleaning(str(curso_ref))

            for key, value in abbreviations.items():
                if fuzz.token_set_ratio(key.lower(), curso_ref_limpo) >= 80:
                    curso_ref_limpo = value


            if fuzz.token_set_ratio(curso_alvo, curso_ref_limpo) >= 80:
                encontrou = True
                break

        if encontrou:
            status_check.append("Consta")
        else:
            status_check.append("Não consta")

    df_base['check_curso'] = status_check

    return df_base


def check_descipline(df_base, df_ref):
    status_check = []

    for disciplina, turma in tqdm(
        iterable= zip(df_base['DISCIPLINA'], df_base['TURMA']),
        desc='VERIFICANDO DISCIPLINAS',
        total= len(df_base),
        unit= "MB",
        colour="yellow"
    ):
        disciplina_alvo = text_cleaning(str(disciplina))
        encontrou_disciplina = False
        
        for diciplina_ref in df_ref["DISCIPLINA"]:
            diciplina_ref_limpo = text_cleaning(str(diciplina_ref))

            if fuzz.token_set_ratio(diciplina_ref_limpo, disciplina_alvo) >= 80:
                encontrou_disciplina = True
                break


        if encontrou_disciplina:
            status_check.append("Consta")
        else:
            status_check.append("Não consta")

    df_base['check_descipline'] = status_check

    return df_base

def check_professor(df_base, df_ref):
    status_check_professor = []
    status_check_diciplina = [] #<- para o futuro
    abbreviations = {
        "erick marrouco":"erick de sousa marouco"
    }

    for professor, diciplina in tqdm(
        iterable= zip(df_base['NOME_PROFESSOR'], df_base['DISCIPLINA']),
        desc='VERIFICANDO PROFESSORES',
        total= len(df_base),
        unit= "MB",
        colour="green"
    ):
        professor_alvo = text_cleaning(str(professor))
        disciplina_alvo = text_cleaning(str(diciplina))

        professor_encontrado = False
        diciplina_encontrado = False #<- para o futuro

        for professor_ref in df_ref["PROFESSORES"]:
            professor_ref_alvo = text_cleaning(professor_ref)
            diciplina_encontrado = True

            for key, value in abbreviations.items():
                if fuzz.token_set_ratio(key, professor_ref_alvo) >= 80: 
                    professor_ref_alvo = value

            if fuzz.token_set_ratio(professor_ref_alvo, professor_alvo) >= 80:
                
                for diciplina_ref in df_ref["DISCIPLINA"]:
                    diciplina_ref_alvo = text_cleaning(diciplina_ref)

                    if fuzz.token_set_ratio(diciplina_ref_alvo, disciplina_alvo) >= 80:
                        professor_encontrado = True

        if professor_encontrado:
            status_check_professor.append("Consta")
        else:
            status_check_professor.append("Não consta")


    df_base['check_professor'] = status_check_professor

    return df_base