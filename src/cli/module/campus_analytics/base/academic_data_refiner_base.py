import re
from time import sleep
import unicodedata

import openpyxl
import pandas as pd
from tqdm import tqdm


from .campus_analytics_core import CampusAnalytics

class AcademicDataRefinerBase(CampusAnalytics):

    def get_total_rows(self, file_path_xlsx:str)-> int:
        wb = openpyxl.load_workbook(file_path_xlsx, read_only=True)
        sheet = wb.active
        total_rows = sheet.max_row
        wb.close()
        return total_rows
    
    def loading(self, temp:float=0.09, colour:str="green"):
        for _ in tqdm(
            iterable=range(100),
            desc= "CARREGANDO DADOS...",
            unit= "MB",
            colour = colour
            ):

            sleep(temp)

    def clean_text(self, text:str)-> str:
        if pd.isna(text):
            return text
        
        text = str(text).strip().lower()
        
        text = unicodedata.normalize("NFKD", text)\
            .encode("ascii", "ignore")\
            .decode("utf-8")
        
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text)
        
        return text