# Definindo uma função simples
def saudacao(nome):
    """
    Retorna uma mensagem de saudação para o nome fornecido.
    """
    return f"Olá, {nome}!"

# Chamar a função e imprimir o resultado
mensagem = saudacao("João")
print(mensagem)  # Saída: Olá, João!

# Função com múltiplos argumentos
def soma(a, b):
    """
    Retorna a soma de dois números.
    """
    return a + b

resultado = soma(3, 4)
print(f"Soma: {resultado}")  # Saída: Soma: 7

# Função com argumentos padrão
def saudacao_completa(nome="Mundo", saudacao="Olá"):
    """
    Retorna uma mensagem de saudação personalizada com argumentos padrão.
    """
    return f"{saudacao}, {nome}!"

# Chamadas da função com e sem argumentos
print(saudacao_completa())                 # Saída: Olá, Mundo!
print(saudacao_completa("Ana"))            # Saída: Olá, Ana!
print(saudacao_completa("Ana", "Oi"))      # Saída: Oi, Ana!

# Função com número variável de argumentos (args)
def listar_numeros(*args):
    """
    Imprime cada número fornecido como argumento.
    """
    for numero in args:
        print(numero)

# Chamar a função com múltiplos argumentos
listar_numeros(1, 2, 3, 4, 5)

# Função com argumentos nomeados (kwargs)
def pessoa_info(**kwargs):
    """
    Retorna informações da pessoa como um dicionário.
    """
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamar a função com argumentos nomeados
pessoa_info(nome="Carlos", idade=28, cidade="São Paulo")

# Funções lambda
soma_lambda = lambda x, y: x + y
print(f"Soma usando lambda: {soma_lambda(5, 7)}")  # Saída: Soma usando lambda: 12

# Uso de lambda com map e filter
numeros = [1, 2, 3, 4, 5, 6]

# Map: Aplicar uma função lambda para dobrar os números
numeros_dobrados = list(map(lambda x: x * 2, numeros))
print(f"Números dobrados usando map: {numeros_dobrados}")  # Saída: [2, 4, 6, 8, 10, 12]

# Filter: Filtrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares usando filter: {numeros_pares}")  # Saída: [2, 4, 6]

# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    """
    Retorna o fatorial de um número.
    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Testar a função recursiva
numero = 5
resultado = fatorial(numero)
print(f"Fatorial de {numero}: {resultado}")  # Saída: Fatorial de 5: 120

# Função recursiva para calcular a série de Fibonacci
def fibonacci(n):
    """
    Retorna o n-ésimo número da série de Fibonacci.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testar a função Fibonacci
n = 10
resultado_fibonacci = fibonacci(n)
print(f"Fibonacci de {n}: {resultado_fibonacci}")  # Saída: Fibonacci de 10: 55
