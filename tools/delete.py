import pandas as pd
import matplotlib.pyplot as plt
import pydotplus

caminhoBase = "final_table.csv"
df = pd.read_csv(caminhoBase)

df.drop(columns=['ebairrnome'],  inplace=True)
df.drop(columns=['eescolruae'],  inplace=True)
df.drop(columns=['anoensino'],  inplace=True)
df.drop(columns=['esermodesc'],  inplace=True)
df.drop(columns=['turma'],  inplace=True)
df.drop(columns=['esitaldesc'],  inplace=True)
df.drop(columns=['TP_CATEGORIA_ESCOLA_PRIVADA'], inplace=True)


df.drop(columns=['nmodennome'],  inplace=True)
df.drop(columns=['nturesnome'],  inplace=True)


df.to_csv("/data/database/fit.csv")
