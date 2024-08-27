import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [10, 14, 18, 24, 30]

# Criando um gráfico de linha simples
plt.plot(x, y)
plt.title('Exemplo de Gráfico de Linha')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Usando Seaborn para um gráfico de dispersão
sns.scatterplot(x=x, y=y)
plt.title('Exemplo de Gráfico de Dispersão')
plt.show()
