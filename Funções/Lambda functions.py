# Funções lambda básicas

# Função lambda para adicionar dois números
soma = lambda x, y: x + y
print(f"Soma usando lambda: {soma(5, 3)}")  # Saída: 8

# Função lambda para elevar um número ao quadrado
quadrado = lambda x: x ** 2
print(f"Quadrado usando lambda: {quadrado(4)}")  # Saída: 16

# Função lambda para verificar se um número é par
eh_par = lambda x: x % 2 == 0
print(f"É par usando lambda: {eh_par(4)}")  # Saída: True
print(f"É par usando lambda: {eh_par(5)}")  # Saída: False

# Funções lambda com map, filter e reduce

# Lista de números para os exemplos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Uso de lambda com map para dobrar os números
numeros_dobrados = list(map(lambda x: x * 2, numeros))
print(f"Números dobrados usando map: {numeros_dobrados}")  # Saída: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Uso de lambda com filter para filtrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares usando filter: {numeros_pares}")  # Saída: [2, 4, 6, 8, 10]

# Uso de lambda com reduce para somar todos os números
from functools import reduce
soma_total = reduce(lambda x, y: x + y, numeros)
print(f"Soma total usando reduce: {soma_total}")  # Saída: 55

# Funções lambda em expressões mais complexas

# Ordenar uma lista de tuplas pela segunda posição usando lambda
tuplas = [(1, 'um'), (2, 'dois'), (3, 'três'), (4, 'quatro')]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(f"Tuplas ordenadas pela segunda posição: {tuplas_ordenadas}")  # Saída: [(4, 'quatro'), (3, 'três'), (2, 'dois'), (1, 'um')]

# Função lambda para calcular o produto de dois números
produto = lambda x, y: x * y
print(f"Produto usando lambda: {produto(5, 3)}")  # Saída: 15

# Função lambda em funções de ordem superior
def aplicar_operacao(x, y, operacao):
    """
    Aplica uma operação fornecida (função) a dois números.
    """
    return operacao(x, y)

# Usar a função aplicar_operacao com uma lambda
resultado_soma = aplicar_operacao(5, 3, lambda x, y: x + y)
resultado_produto = aplicar_operacao(5, 3, lambda x, y: x * y)
print(f"Resultado da soma usando função de ordem superior: {resultado_soma}")  # Saída: 8
print(f"Resultado do produto usando função de ordem superior: {resultado_produto}")  # Saída: 15

# Funções lambda dentro de listas e dicionários

# Lista de funções lambda
funcoes_lambda = [
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: x * 2,
    lambda x: x / 2
]

# Aplicar cada função lambda a um número
numero = 4
for func in funcoes_lambda:
    print(func(numero))  # Saída: 5, 3, 8, 2

# Dicionário de funções lambda
operacoes = {
    "soma": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    "multiplicacao": lambda x, y: x * y,
    "divisao": lambda x, y: x / y if y != 0 else float('inf')
}

# Usar funções lambda do dicionário
print(f"Soma: {operacoes['soma'](10, 5)}")           # Saída: 15
print(f"Subtração: {operacoes['subtracao'](10, 5)}") # Saída: 5
print(f"Multiplicação: {operacoes['multiplicacao'](10, 5)}") # Saída: 50
print(f"Divisão: {operacoes['divisao'](10, 5)}")     # Saída: 2.0
