import pandas as pd
import numpy as np

# Criando um DataFrame com dados faltantes
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
}
df = pd.DataFrame(data)

# Exibindo os dados faltantes
print(df)

# Preenchendo valores faltantes com a média
df.fillna(df.mean(), inplace=True)
print(df)

# Removendo linhas com valores faltantes
df.dropna(inplace=True)
print(df)
