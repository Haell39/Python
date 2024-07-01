# Explicando Matrizes em Python

# Matrizes com Listas Aninhadas

# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Função para imprimir uma matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

print("Matriz original:")
imprimir_matriz(matriz)

# Acessando o elemento na linha 2, coluna 3 (elemento 6)
elemento = matriz[1][2]
print(f"\nElemento na linha 2, coluna 3: {elemento}")

# Modificando o elemento na linha 1, coluna 1 para 10
matriz[0][0] = 10
print("\nMatriz após modificação:")
imprimir_matriz(matriz)

# Adicionando uma nova linha à matriz
nova_linha = [10, 11, 12]
matriz.append(nova_linha)
print("\nMatriz após adicionar nova linha:")
imprimir_matriz(matriz)

# Removendo a última linha da matriz
matriz.pop()
print("\nMatriz após remover a última linha:")
imprimir_matriz(matriz)

# Utilizando a biblioteca NumPy para operações mais avançadas

import numpy as np

# Criando uma matriz 3x3 com NumPy
matriz_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nMatriz NumPy:")
print(matriz_np)

# Acessando o elemento na linha 2, coluna 3
elemento_np = matriz_np[1, 2]
print(f"\nElemento na linha 2, coluna 3 (NumPy): {elemento_np}")

# Modificando o elemento na linha 1, coluna 1 para 10
matriz_np[0, 0] = 10
print("\nMatriz NumPy após modificação:")
print(matriz_np)

# Somando duas matrizes
matriz_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matriz_b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

soma = matriz_a + matriz_b
print("\nSoma das matrizes (NumPy):")
print(soma)

# Multiplicação de Matrizes
produto = np.dot(matriz_a, matriz_b)
print("\nProduto das matrizes (NumPy):")
print(produto)

# Função para somar e multiplicar duas matrizes
def soma_e_produto(matriz1, matriz2):
    # Verificar se as dimensões são compatíveis
    if matriz1.shape != matriz2.shape:
        raise ValueError("As matrizes devem ter as mesmas dimensões para a soma.")
    
    if matriz1.shape[1] != matriz2.shape[0]:
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda para o produto.")
    
    soma = matriz1 + matriz2
    produto = np.dot(matriz1, matriz2)
    
    return soma, produto

# Matrizes de exemplo para a função soma_e_produto
matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matriz2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Soma e produto
soma, produto = soma_e_produto(matriz1, matriz2)
print("\nSoma das matrizes (função):")
print(soma)
print("\nProduto das matrizes (função):")
print(produto)
