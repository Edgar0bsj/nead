from operator import itemgetter
import threading

import pandas as pd

from src.cli.util.loading import loading

def xlsx_parse_df(path_arquivo:str, df_temp:dict, key:str)-> pd.DataFrame:

    df = pd.read_excel(path_arquivo)
    
    df_temp[key] = df


def create_dataframe(data_base, data_ref)-> dict[str,pd.DataFrame]:
    dfs = {}
    
    t1 = threading.Thread(
        target = loading
    )
    t2 = threading.Thread(
        target = xlsx_parse_df,
        args=(data_base, dfs, "data_base")
    )
    t3 = threading.Thread(
        target = xlsx_parse_df,
        args = (data_ref, dfs, "data_ref")
    )
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    return dfs

def getDataFrame(path_data_base, path_data_ref):
    return itemgetter("data_base","data_ref")(create_dataframe(path_data_base, path_data_ref))