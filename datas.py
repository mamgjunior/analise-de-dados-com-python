import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

#Fazendo a leitura dos arquivos
df_aracaju = pd.read_excel("datasets/xls/Aracaju.xlsx")
df_fortaleza = pd.read_excel("datasets/xls/Fortaleza.xlsx")
df_natal = pd.read_excel("datasets/xls/Natal.xlsx")
df_recife = pd.read_excel("datasets/xls/Recife.xlsx")
df_salvador = pd.read_excel("datasets/xls/Salvador.xlsx")

#Juntando todos os arquivos
df = pd.concat([df_aracaju, df_fortaleza, df_natal, df_recife, df_salvador])

df["Receita"] = df["Vendas"].mul(df["Qtde"])

#Transformando a coluna de datas em datetime
df["Data"] = pd.to_datetime(df["Data"])

print(df.dtypes)

#Exibindo informações agrupadas por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

#Criando uma coluna de ano da vendas
df["ano_venda"] = df["Data"].dt.year
print(df.sample(5))

df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.sample(5))

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))

#Criando uma coluna com o trimestre das vendas
df["trimestre_venda"] = df["Data"].dt.quarter
print(df.sample(5))

#Exibindo os dados no ano de 2019 no mês de março
vendas_marco = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco)
