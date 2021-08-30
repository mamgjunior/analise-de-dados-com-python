from numpy import rint
import pandas as pd
import matplotlib.pyplot as plt

#Estilizando
plt.style.use("seaborn")

#Criando o dataframe
df = pd.read_excel("datasets/xls/AdventureWorks.xlsx")

print("- Exibindo as 5 primeiras linhas do dataframe:")
print(df.head())

print("\n- Exibindo a quantidade de linhas e colunas:")
print(df.shape)

print("\n- Exibindo os tipos de dados existentes:")
print(df.dtypes)

receita_total = df["Valor Venda"].sum()
print("\n- Qual foi a receita total?\nR: " + str(receita_total))

#Criando uma coluna de custo
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])
print("\n- Qual o custo total?\nR: "+ str(round(df["custo"].sum(), 2)))

#Criando uma coluna de lucro
df["lucro"] = df["Valor Venda"] - df["custo"]
print("\n- Qual o total de lucro?\nR: "+ str(round(df["lucro"].sum(), 2)))

#Criando uma coluna de tempo de envio
df["tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print("\nTestando a nova estrutura com a coluna tempo de envio adicionada:")
print(df.head(1))

#Exibindo a média de tempo de envio por marca
print("\n- Exibindo a média de tempo de envio por marca:")
print(df.groupby("Marca")["tempo_envio"].mean())

#Exibindo a quantidade dados faltantes
print("\n- Exibindo a quantidade dados faltantes:\nR:" + str(df.isnull().sum()))

#Agrupando por ano e marca
print("\n- Agrupando por ano e marca:")
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())

#Configurando o formato de numeros flutuantes
pd.options.display.float_format = "{:20,.2f}".format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano)

#Exibindo um totalizador dos produtos
print("\n- Exibindo um totalizador dos produtos:")
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

#Exibindo o total de produtos vendidos em um grafico
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produtos")
plt.show()

#Exibindo o lucro por ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009)

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro X Mês")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro X Mês")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal")
plt.show()


df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro X Mês")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal")
plt.show()

df["Tempo_envio"].describe()

#Grafico de boxplot
plt.boxplot(df["Tempo_envio"])
plt.show()

plt.hist(df["Tempo_envio"])
plt.show()
 
#Criando um csv
# df.to_csv("df_vendas_novo.csv", index=False)