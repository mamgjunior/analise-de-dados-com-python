import pandas as pd

#Fazendo a leitura dos arquivos
df_aracaju = pd.read_excel("datasets/xls/Aracaju.xlsx")
df_fortaleza = pd.read_excel("datasets/xls/Fortaleza.xlsx")
df_natal = pd.read_excel("datasets/xls/Natal.xlsx")
df_recife = pd.read_excel("datasets/xls/Recife.xlsx")
df_salvador = pd.read_excel("datasets/xls/Salvador.xlsx")

#Exibindo informações
print("*** Aracaju ***")
print(df_aracaju.head())
print("*******************************************\n")

print("*** Fortaleza ***")
print(df_fortaleza.head())
print("*******************************************\n")

print("*** Natal ***")
print(df_natal.head())
print("*******************************************\n")

print("*** Recife ***")
print(df_recife.head())
print("*******************************************\n")

print("*** Salvador ***")
print(df_salvador.head())
print("*******************************************\n")

#Juntando todos os arquivos
df = pd.concat([df_aracaju, df_fortaleza, df_natal, df_recife, df_salvador])

print("*** Todas as cidades juntas ***")
print(df.head())
print("*******************************************\n")

#Exibindo uma amostra do conjunto de dados
print(df.sample(8))

#Exibindo o tipo de dados de cada coluna
print(df.dtypes)

#Alterando um tipo de dado de uma coluna
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)

#Consultando quanto valores nulos existem em cada coluna
print(df.isnull().sum())

#Substituir os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

#Substituir os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando linhas com valores nulos
df.dropna(inplace=True)

#Apagando linhas com valores nulos por uma coluna especifica
df.dropna(subset=["Vendas"], inplace=True)

#Apagando linhas com valores nulos em todas as colunas
df.dropna(how="all", inplace=True)

#Criando uma nova coluna apartir de colunas existentes
#Exemplo1:
df["Receita"] = df["Vendas"].mul(df["Qtde"])

#Exemplo2:
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

#Maior receira
print(df["Receita"].max())

#Menor receita
print(df["Receita"].min())

#Exibindo as 3 maiores receitas
print(df.nlargest(3, "Receita"))

#Exibindo as 3 menores receitas
print(df.nsmallest(3, "Receita"))

#Exibindo a soma das reitas por cidades ou seja agrupando por cidade
print(df.groupby("Cidade")["Receita"].sum())

#Exibindo os dados de forma ordenada por uma coluna especifica, da maior para manor
print(df.sort_values("Receita", ascending=False).head(10))
