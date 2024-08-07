import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criar um DataFrame simples com pandas
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)
print("DataFrame criado com sucesso:")
print(df)

# Criar um gráfico simples com seaborn
sns.set(style="darkgrid")
sns.lineplot(x='A', y='B', data=df)
plt.title("Gráfico de Linha Simples")
plt.show()
