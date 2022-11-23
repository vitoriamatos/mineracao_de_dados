import pandas as pd
import matplotlib.pyplot as plt
import pydotplus

caminhoBase = "data/database/fit.csv"
df = pd.read_csv(caminhoBase)

# df.drop(columns=['ebairrnome'],  inplace=True)
# df.drop(columns=['anoensino'],  inplace=True)
# df.drop(columns=['esermodesc'],  inplace=True)
# df.drop(columns=['nturesnome'],  inplace=True)
# df.drop(columns=['IN_DEPENDENCIAS_PNE'], inplace=True)
# df.drop(columns=['IN_SECRETARIA'], inplace=True)
# df.drop(columns=['IN_BANHEIRO_CHUVEIRO'], inplace=True)
# df.drop(columns=['IN_REGULAR_x'], inplace=True)
# df.drop(columns=['IN_EJA_x'], inplace=True)
# df.drop(columns=['IN_PROFISSIONALIZANTE_x'], inplace=True)
df.drop(columns=['id'],  inplace=True)
df.drop(columns=['ID_MATRICULA'],  inplace=True)

df.to_csv("data/database/data.csv")
