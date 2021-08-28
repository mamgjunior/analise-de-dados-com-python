import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

#Criando meu dataframe
df = pd.read_csv("datasets/csv/Gapminder.csv", error_bad_lines=False, sep=";")

#Exibindo algumas informações do dataframe
print(df.head())

#Renomeando as colunas
df = df.rename(columns={
    "country": "País",
    "continent": "Continente",
    "year": "Ano",
    "lifeExp": "Expectativa de vida",
    "pop": "População",
    "gdpPercap": "PIB"
})
print(df.head())

#Retornando o total de linhas e colunas
print("Total de linhas: " + str(df.shape[0]))
print("Total de colunas: " + str(df.shape[1]))

#Exibindo os nomes das colunas
print(df.columns)

#Exibindo os tipos de dados inclusos no dataframe
print(df.dtypes)

#Exibindo as ultimas linhas ou seja o contrario do head
print(df.tail())

#Exibindo informações estátisticas dos dados
print(df.describe())

#Exibindo os continentes sem duplicidadas
print(df["Continente"].unique())

#Pegando dados expecificos
oceania = df.loc[df["Continente"] == "Oceania"]
print(oceania.head())

#Agrupando dados de forma unica
print(df.groupby("Continente")["País"].nunique())

#Exibindo a expectativa de vida media por ano
print(df.groupby("Ano")["Expectativa de vida"].mean())

#Exibindo a média do PIB
print(df["PIB"].mean())
