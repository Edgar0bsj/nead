from src.multi_docencia_insights.mdi import Mdi
from src.data_cross_referencing_analysis.analysis import data_cross_referencing_analysis


df = Mdi().init()


print(df.head())
print(df.info())

# print(df.head())
# print(df.info())
# print(df.isnull().sum())
