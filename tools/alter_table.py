import pandas as pd
import matplotlib.pyplot as plt
import pydotplus

caminhoBase = "final_table.csv"
df = pd.read_csv(caminhoBase)

# Transformando a tabela alunosexo em Númerica

df.loc[df['alunosexo'] == 'F', 'alunosexo'] = 1
df.loc[df['alunosexo'] == 'M', 'alunosexo'] = 2


# Transformando a tabela Situ em Númerica

df['situ'== 'AP'] = 1
df.loc[df['situ'] == 'AP', 'situ'] = 1
df.loc[df['situ'] == 'RT', 'situ'] = 2
df.loc[df['situ'] == 'TR', 'situ'] = 3
df.loc[df['situ'] == 'RN', 'situ'] = 4
df.loc[df['situ'] == 'TA', 'situ'] = 5
df.loc[df['situ'] == 'D', 'situ'] = 6
df.loc[df['situ'] == 'RF', 'situ'] = 7
df.loc[df['situ'] == 'MO', 'situ'] = 8
df.loc[df['situ'] == 'TS', 'situ'] = 9
df.loc[df['situ'] == 'FA', 'situ'] = 10
df.loc[df['situ'] == 'DERN', 'situ'] = 11
df.loc[df['situ'] == 'NC', 'situ'] = 12
df.loc[df['situ'] == 'DETA', 'situ'] =  13
df.loc[df['situ'] == 'RTTA', 'situ'] = 14

df.to_csv("tabela2.csv")
