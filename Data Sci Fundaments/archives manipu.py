import pandas as pd

# Carregando dados de um arquivo CSV
df = pd.read_csv('dados.csv')
print(df.head())

# Salvando um DataFrame como Excel
df.to_excel('dados.xlsx', index=False)
