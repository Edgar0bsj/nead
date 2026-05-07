from src.multi_docencia_insights.mdi import Mdi
from src.data_cross_referencing_analysis.analysis import data_cross_referencing_analysis


mdi = Mdi()

df = mdi.getDf()

mdi.save_to_excel()


print(df.head())
print(df.info())
print(df.to_markdown(index=False))


# print(df.head())
# print(df.info())
# print(df.isnull().sum())
