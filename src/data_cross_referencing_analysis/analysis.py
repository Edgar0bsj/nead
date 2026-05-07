import numpy as np

from src.data_cross_referencing_analysis.data_cleaning import cleaningData
from src.data_cross_referencing_analysis.data_loader import loaderData


def data_cross_referencing_analysis():
    df, dff = loaderData()
    df, dff = cleaningData(df, dff)

    df_merge = df.merge(
        dff,
        on=['CURSO','PERIODO','NOME_PROFESSOR'],
        how="outer",
        indicator=True
    )

    df_merge["STATUS"] = np.select(
        [
            df_merge["_merge"] == "both",
            df_merge["_merge"] == "left_only",
            df_merge["_merge"] == "right_only",
        ],
        [
            "OK",
            "SOMENTE_SOPHIA",
            "SOMENTE_NA_PLANILHA"
        ],
        default="..."
    )

    df_merge = df_merge[['TURMA', 'CURSO', 'PERIODO', 'DISCIPLINA_SOPHIA', 'DISCIPLINA_PLANILHA','NOME_PROFESSOR', 'STATUS']]


    print(df_merge.head())
    df_merge.to_excel("data_cross_referencing_analysis.xlsx",index=False)

    return None