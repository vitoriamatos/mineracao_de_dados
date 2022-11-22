import pandas as pd
import matplotlib.pyplot as plt

caminhoBase = "data/database/database_main.csv"
df2 = pd.read_csv(caminhoBase, delimiter = ",", encoding = "ISO-8859-1")

caminhoBase2 = "data/controller/controller_main.csv"
decisoes = pd.read_csv(caminhoBase2, delimiter = ",", encoding = "ISO-8859-1")

excluir = []
for index, row in decisoes.iterrows():
  nomeAtributo = row['nome']
  decisaoAtributo = row['decisao']
  if decisaoAtributo == 'c':
    print(df2[nomeAtributo]);
    df2[nomeAtributo] = df2[nomeAtributo].astype('category') #mudando tipo do dado
  elif decisaoAtributo == 'n':
    print(df2[nomeAtributo]);
    df2[nomeAtributo] = df2[nomeAtributo].astype('float64') #mudando tipo do dado
  elif decisaoAtributo == 'e':
    df2.drop(columns = [nomeAtributo], inplace=True) #adicionando atributos que serão exluídos.
  else:  
    print("Atributos excluído: ", nomeAtributo)
    df2 = df2.drop(columns = [nomeAtributo]) #excluir colunas

df2.to_csv("data/database/database_fit.csv")