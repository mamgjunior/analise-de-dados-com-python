import pandas as pd
import matplotlib.pyplot as plt

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

df["ano_venda"] = df["Data"].dt.year
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

#Exibindo um grafico de barras
df["LojaID"].value_counts(ascending=False).plot.bar(title="Vendas por loja")
plt.xlabel("Lojas")
plt.ylabel("Total vendas")
plt.show()

#Exibindo um grafico de barras horizontais
# df["LojaID"].value_counts(ascending=False).plot.barh()

#Exibindo grafico de pizza
# df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Exibindo total de vendas por cidade
df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade")
plt.xlabel("Cidade")
plt.ylabel("Total de vendas")
plt.show()

#Alterando a cor do grafico
#df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color="red")

#Alterando o stylo
plt.style.use("ggplot")
df.groupby(df["mes_venda"])["Qtde"].sum().plot()
plt.xlabel("Mês")
plt.ylabel("Total produtos vendidos")
plt.legend()
plt.show()

#Selecionando as vendas de 2019
df_2019 = df[df["ano_venda"] == 2019]

#total de produtos vendidos no mês
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="o")
plt.xlabel("Mês")
plt.ylabel("Total produtos vendidos")
plt.legend()
plt.show()

#Hisograma
plt.hist(df["Qtde"], color="blue")
plt.show()

#Exibindo um grafico de dispersão
plt.scatter(x=df["dia_venda"], y=df_2019["Receita"])
plt.show()

#Salvando um grafico apos exibir
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="o")
plt.xlabel("Mês")
plt.ylabel("Total produtos vendidos")
plt.legend()
plt.show()
plt.savefig("Grafico.png")