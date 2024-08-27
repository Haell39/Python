import pandas as pd

# Criando um DataFrame de exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 35]
}
df = pd.DataFrame(data)

# Definindo uma função para aplicar aos dados
def add_years(age):
    return age + 5

# Aplicando a função em uma coluna
df['Idade + 5'] = df['Idade'].apply(add_years)
print(df)

# Usando lambda para aplicar a função
df['Idade + 5'] = df['Idade'].apply(lambda x: x + 5)
print(df)
