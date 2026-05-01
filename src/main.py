from src.lib.teacher_audit import *

sistema = TeacherSheetReviewer(
    base_file_path = "C:/Users/unig.ead/Documents/analysis/src/data/base.xlsx",
    reference_file_path= "C:/Users/unig.ead/Documents/analysis/src/data/ref.xlsx",
    base_column_mapping= {
        "DISCIPLINA":"",
        "MODALIDADE":"",
        "POLO":"",
        "PROFESSOR":"",
        "TURMA":""
        },
    base_filter_values= {"MODALIDADE":"", "POLO":""},
    reference_column_mapping={
        "CURSO":"",
        "DISCIPLINA":"",
        "PERIODO":"",
        "PROFESSOR":""
    },
    abbreviation_mapping={}
)

print(type(sistema.base_file_path))
# sistema.initialize()