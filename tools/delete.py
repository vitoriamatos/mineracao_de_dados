import pandas as pd
import matplotlib.pyplot as plt
import pydotplus

caminhoBase = "data/database/evasao-escolar2.csv"
df = pd.read_csv(caminhoBase)



df.drop(columns=['id'], inplace=True)
df.drop(columns=['nivelbairro'], inplace=True)
df.drop(columns=['IN_COZINHA'], inplace=True)
df.drop(columns=['serie'], inplace=True)



df.to_csv("data/database/evasao-escolar3.csv")
