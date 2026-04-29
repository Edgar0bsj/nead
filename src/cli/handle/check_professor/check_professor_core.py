from src.cli.handle.check_professor.checks import check_courses, check_descipline
from src.cli.handle.check_professor.clear_df import clear_data
from src.cli.handle.check_professor.create_dataframe import getDataFrame
from src.cli.util.check_if_file_exists import check_if_file_exists
from time import sleep


def check_professor_core(path_data_base:str, path_data_ref:str):
    try:

        check_if_file_exists(path_data_base)
        check_if_file_exists(path_data_ref)
        df_base, df_ref = getDataFrame(path_data_base, path_data_ref)
        df_base, df_ref = clear_data(df_base, df_ref, entrada=2)
        
        df_base = check_courses(df_base, df_ref)
        sleep(0.3)
        df_base = check_descipline(df_base, df_ref)


#========================================= TESTE

        # consta = df_base[df_base['check_curso'] == 'Não consta']
        consta = df_base[df_base['check_descipline'] == 'Consta']
        print(consta.head())
        input(" ")

    except ImportError as err:
        print(err)
        input("Enter para continuar...")
    except Exception as err:
        print("QUEBROUUUUUUUU")
        print(err)
        raise
