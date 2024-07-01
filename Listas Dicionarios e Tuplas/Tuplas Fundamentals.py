# Explicando Tuplas em Python

# Tuplas Básicas

# Criando tuplas
tupla_vazia = ()
tupla_simples = (1, 2, 3)

print("Tupla Vazia:", tupla_vazia)
print("Tupla Simples:", tupla_simples)

# Tuplas com diferentes tipos de dados
tupla_mista = (1, "Hello", 3.14)
print("Tupla Mista:", tupla_mista)

# Acessando elementos da tupla
primeiro_elemento = tupla_simples[0]
ultimo_elemento = tupla_simples[-1]
print("\nPrimeiro Elemento da Tupla Simples:", primeiro_elemento)
print("Último Elemento da Tupla Simples:", ultimo_elemento)

# Tentando modificar um elemento da tupla (gera erro)
try:
    tupla_simples[0] = 10
except TypeError as e:
    print("\nErro ao tentar modificar a tupla:", e)

# Operações com Tuplas

# Concatenando tuplas
tupla_concatenada = tupla_simples + tupla_mista
print("\nTupla Concatenada:", tupla_concatenada)

# Repetindo tuplas
tupla_repetida = tupla_simples * 2
print("Tupla Repetida:", tupla_repetida)

# Desempacotamento de Tuplas

# Desempacotando uma tupla em variáveis
a, b, c = tupla_simples
print("\nDesempacotamento da Tupla Simples:")
print("a:", a)
print("b:", b)
print("c:", c)

# Usando * para desempacotar o restante dos elementos
tupla_expandida = (1, 2, 3, 4, 5)
x, y, *resto = tupla_expandida
print("\nDesempacotamento com *:")
print("x:", x)
print("y:", y)
print("resto:", resto)

# Funções e Métodos Úteis para Tuplas

# Comprimento de uma tupla
comprimento = len(tupla_simples)
print("\nComprimento da Tupla Simples:", comprimento)

# Contagem de um elemento específico na tupla
contagem = tupla_concatenada.count(1)
print("Contagem do elemento 1 na Tupla Concatenada:", contagem)

# Índice de um elemento específico na tupla
indice = tupla_concatenada.index("Hello")
print('Índice do elemento "Hello" na Tupla Concatenada:', indice)

# Função que retorna a soma e o produto dos elementos de uma tupla de números

def soma_e_produto(tupla):
    soma = sum(tupla)
    produto = 1
    for num in tupla:
        produto *= num
    return soma, produto

# Exemplo de uso da função soma_e_produto
tupla_numeros = (1, 2, 3, 4)
soma, produto = soma_e_produto(tupla_numeros)
print("\nSoma e Produto dos elementos da Tupla de Números:")
print("Tupla:", tupla_numeros)
print("Soma:", soma)
print("Produto:", produto)

# Tuplas Aninhadas

# Criando uma tupla de tuplas
tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print("\nTupla Aninhada:", tupla_aninhada)

# Acessando elementos em uma tupla aninhada
elemento_aninhado = tupla_aninhada[1][1]
print("Elemento na posição [1][1] da Tupla Aninhada:", elemento_aninhado)

# Desafio Prático

# Função que encontra o maior e o menor elemento em uma tupla de números

def maior_e_menor(tupla):
    maior = max(tupla)
    menor = min(tupla)
    return maior, menor

# Exemplo de uso da função maior_e_menor
maior, menor = maior_e_menor(tupla_numeros)
print("\nMaior e Menor elementos da Tupla de Números:")
print("Tupla:", tupla_numeros)
print("Maior:", maior)
print("Menor:", menor)
