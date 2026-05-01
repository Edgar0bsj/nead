from .campus_analytics import AcademicDataRefiner, filters_config
# ==============================================
# DADOS NECESSARIO PARA INSTANCIAR
# ==============================================
file_path_xlsx = "C:/Users/unig.ead/Documents/analysis/src/data/base.xlsx"
columns = ["POLO","MODALIDADE","TURMA","DISCIPLINA","NOME_PROFESSOR"]
filters = [
    filters_config("POLO", "Nova Iguaçu"),
    filters_config("MODALIDADE", "G"),
    filters_config("TURMA", r'\.2\.\dP', isRegex=True)
]

# ==============================================
# INSTANCIANDO ENTIDADE
# ==============================================
academicDataRefiner = AcademicDataRefiner(
    file_path_xlsx= file_path_xlsx,
    columns=columns,
    filters=filters
)

# ==============================================
# EXECUTANDO OPERAÇÕES
# ==============================================
df_base = academicDataRefiner.initialize()
print(df_base.head(20))


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ==============================================
# DADOS NECESSARIO PARA INSTANCIAR
# ==============================================
file_path_xlsx = "C:/Users/unig.ead/Documents/analysis/src/data/ref.xlsx"
columns = ["CURSO","PERÍODO","DISCIPLINA","PROFESSORES"]

# ==============================================
# INSTANCIANDO ENTIDADE
# ==============================================
academicDataRefiner2 = AcademicDataRefiner(
    file_path_xlsx= file_path_xlsx,
    columns=columns
)

# ==============================================
# EXECUTANDO OPERAÇÕES
# ==============================================
df_ref = academicDataRefiner2.initialize()
print(df_ref.head(20))
