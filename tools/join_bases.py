import pandas as pd
import matplotlib.pyplot as plt

### Leitura base
caminhoBase = "join.csv"
df_a = pd.read_csv(caminhoBase, delimiter=',', encoding = "ISO-8859-1")
caminhoBase = "situacaofinalalunos2018.csv"
df_t = pd.read_csv(caminhoBase, delimiter = ";", encoding = "ISO-8859-1")

### Junção das bases

df = pd.merge(df_a, df_t, how="left", on=["nturesnome", "nturesnome"])
df.to_csv("join_table.csv")