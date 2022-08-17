from pickle import NONE
import pandas as pd
import openpyxl

df = pd.read_excel("111年1月-110年1月.xlsx", sheet_name=None,usecols="C")
print(df)
cell = df.at[14," 111年1月\nJanuary, 2022"]
print(cell)