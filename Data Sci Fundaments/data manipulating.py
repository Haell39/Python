import pandas as pd

# Criando um DataFrame simples
data = {
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)

# Selecionando uma coluna
print(df['Nome'])

# Filtrando dados
print(df[df['Idade'] > 30])
