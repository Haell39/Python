import pandas as pd

# Criando um DataFrame de exemplo
data = {
    'Categoria': ['A', 'B', 'A', 'B', 'A'],
    'Valor': [10, 15, 10, 20, 25]
}
df = pd.DataFrame(data)

# Agrupando os dados por categoria e somando os valores
grouped = df.groupby('Categoria').sum()
print(grouped)

# Calculando a média dos valores por categoria
mean_values = df.groupby('Categoria').mean()
print(mean_values)
