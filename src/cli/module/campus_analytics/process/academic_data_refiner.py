import unicodedata
from dataclasses import dataclass
from pathlib import Path
import threading
from typing import Optional
import pandas as pd
from ..base.academic_data_refiner_base import AcademicDataRefinerBase

#====================================================

@dataclass
class filters_config:
    df_filter:str
    value_filter:str
    isRegex:str = False

#====================================================

class AcademicDataRefiner(AcademicDataRefinerBase):
    def __init__(self,
        file_path_xlsx:str,
        columns:list[str],
        filters:Optional[list[filters_config]]= None
        )-> None:

        self.file_path_xlsx = file_path_xlsx
        self.columns = columns
        self.filters = filters

    def initialize(self)-> pd.DataFrame:
        df = self.load_spreadsheet(self.file_path_xlsx)
        df = self.select_columns(df)
        df = self.lowercase_trim_fields(df)
        df = self.remove_accents(df)
        df = self.clean_special_characters(df)
        df = self.handle_missing_values(df)
        df = self.normalize_text(df)

        return df

    def load_spreadsheet(self, path_xlsx:str)-> pd.DataFrame:

        if not Path(path_xlsx).exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {path_xlsx}"
            )
        
        def thread_read_excel(result:list, file_path_xlsx:str):
            df = pd.read_excel(file_path_xlsx)
            result.append(df)

        result:list[pd.DataFrame] = []
        threads:dict[function,Optional[tuple]] = {
            thread_read_excel: (result, path_xlsx),
            super().loading: None
        }

        times:list[threading.Thread] = []

        for func, arg in threads.items():
            if arg is None: arg = ()
            t = threading.Thread(
                target= func,
                args= arg
                )
            times.append(t)

        for time in times: time.start()
        for time in times: time.join()
        
        return result[0]
    
    def select_columns(self, df:pd.DataFrame)-> pd.DataFrame:
        
        dataframe = df[self.columns]

        if self.filters is not None :
            for conf in self.filters:
                if not conf.isRegex:
                    dataframe = dataframe[dataframe[conf.df_filter] == conf.value_filter]
                else:
                    dataframe = dataframe[dataframe[conf.df_filter].str.contains(conf.value_filter, regex=True)]
        
        return dataframe

    def lowercase_trim_fields(self, df:pd.DataFrame)-> pd.DataFrame:

        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
            df[col] = df[col].str.lower()

        return df
            
    def remove_accents(self, df:pd.DataFrame)-> pd.DataFrame:
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].fillna("")
            df[col] = df[col].apply(lambda texto: unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("utf-8"))
        
        return df
    
    def clean_special_characters(self, df:pd.DataFrame):
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)
        
        return df
        
    def handle_missing_values(self, df:pd.DataFrame):
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].replace(["", " ", "nan", "None"], None)
        
        return df

    def normalize_text(self, df:pd.DataFrame):

        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(super().clean_text)
        
        return df