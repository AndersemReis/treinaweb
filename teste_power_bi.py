import pandas as pd

arquivo = pd.read_excel("C:\Users\Familia_Souza\OneDrive\Documentos\aulas - Treinaweb\teste.xlsx")

tam = len(arquivo)

for i in range(tam):
    teste = arquivo[i]


