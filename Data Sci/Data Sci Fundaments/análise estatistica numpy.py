import numpy as np

# Criando arrays Numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Operações matemáticas básicas
print("Soma:", np.sum(arr))
print("Média:", np.mean(arr))
print("Desvio Padrão:", np.std(arr))

# Operações entre arrays
arr2 = np.array([10, 20, 30, 40, 50])
print("Soma de arrays:", arr + arr2)
