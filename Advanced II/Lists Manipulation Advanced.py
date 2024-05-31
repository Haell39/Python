# Lista inicial de números
numeros = [5, 2, 9, 1, 5, 6]

# Iterar sobre a lista e imprimir cada número
print("Iteração sobre a lista:")
for numero in numeros:
    print(numero)

# Multiplicar cada número por 2 e criar uma nova lista (compreensão de listas)
numeros_dobrados = [numero * 2 for numero in numeros]
print("\nLista com números dobrados:")
print(numeros_dobrados)

# Filtrar números pares da lista original
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print("\nLista com números pares:")
print(numeros_pares)

# Elevar cada número ao quadrado e criar uma nova lista
numeros_ao_quadrado = [numero ** 2 for numero in numeros]
print("\nLista com números ao quadrado:")
print(numeros_ao_quadrado)

# Ordenar a lista original em ordem crescente
numeros_ordenados = sorted(numeros)
print("\nLista ordenada em ordem crescente:")
print(numeros_ordenados)

# Ordenar a lista original em ordem decrescente
numeros_ordenados_decrescente = sorted(numeros, reverse=True)
print("\nLista ordenada em ordem decrescente:")
print(numeros_ordenados_decrescente)

# Remover duplicatas da lista (usando set)
numeros_unicos = list(set(numeros))
print("\nLista sem duplicatas:")
print(numeros_unicos)

# Funções embutidas: max, min, sum
max_numero = max(numeros)
min_numero = min(numeros)
soma_numeros = sum(numeros)

print("\nFunções embutidas:")
print(f"Máximo: {max_numero}")
print(f"Mínimo: {min_numero}")
print(f"Soma: {soma_numeros}")

# Função embutida: map para aplicar uma função a cada elemento da lista
def triplo(x):
    return x * 3

numeros_triplos = list(map(triplo, numeros))
print("\nLista com números triplicados (usando map):")
print(numeros_triplos)

# Função embutida: filter para filtrar elementos da lista
numeros_maiores_que_cinco = list(filter(lambda x: x > 5, numeros))
print("\nLista com números maiores que 5 (usando filter):")
print(numeros_maiores_que_cinco)

# Função embutida: reduce para aplicar uma função cumulativamente aos elementos da lista
from functools import reduce

def produto(a, b):
    return a * b

produto_total = reduce(produto, numeros)
print("\nProduto total dos números (usando reduce):")
print(produto_total)

# List comprehension aninhada (matriz 3x3)
matriz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("\nMatriz 3x3 criada com list comprehension aninhada:")
for linha in matriz:
    print(linha)

# Flattening a list of lists (convertendo uma matriz para uma lista)
matriz_flat = [item for sublist in matriz for item in sublist]
print("\nMatriz 'flattened' (convertida para lista):")
print(matriz_flat)
