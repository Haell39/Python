# Função recursiva básica: Calcular o fatorial de um número
def fatorial(n):
    """
    Retorna o fatorial de um número.
    O fatorial de n (n!) é o produto de todos os inteiros positivos até n.
    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Testar a função fatorial
numero = 5
resultado_fatorial = fatorial(numero)
print(f"Fatorial de {numero}: {resultado_fatorial}")  # Saída: Fatorial de 5: 120

# Função recursiva para calcular o n-ésimo número da série de Fibonacci
def fibonacci(n):
    """
    Retorna o n-ésimo número da série de Fibonacci.
    A série de Fibonacci é uma sequência onde cada número é a soma dos dois anteriores.
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

# Função recursiva para encontrar o maior divisor comum (MDC) de dois números
def mdc(a, b):
    """
    Retorna o maior divisor comum (MDC) de dois números usando o algoritmo de Euclides.
    """
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Testar a função MDC
a, b = 48, 18
resultado_mdc = mdc(a, b)
print(f"MDC de {a} e {b}: {resultado_mdc}")  # Saída: MDC de 48 e 18: 6

# Função recursiva para somar os elementos de uma lista
def soma_lista(lista):
    """
    Retorna a soma dos elementos de uma lista.
    """
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# Testar a função soma_lista
lista_numeros = [1, 2, 3, 4, 5]
resultado_soma_lista = soma_lista(lista_numeros)
print(f"Soma dos elementos da lista: {resultado_soma_lista}")  # Saída: Soma dos elementos da lista: 15

# Função recursiva para inverter uma string
def inverter_string(s):
    """
    Retorna a string invertida.
    """
    if len(s) == 0:
        return s
    else:
        return s[-1] + inverter_string(s[:-1])

# Testar a função inverter_string
string = "recursão"
resultado_inverter_string = inverter_string(string)
print(f"String invertida: {resultado_inverter_string}")  # Saída: String invertida: oãsrucre

# Função recursiva para resolver o problema das torres de Hanói
def torres_de_hanoi(n, origem, destino, auxiliar):
    """
    Resolve o problema das torres de Hanói.
    """
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origem)

# Testar a função torres_de_hanoi
n_discos = 3
print("\nMovimentos para resolver as torres de Hanói com 3 discos:")
torres_de_hanoi(n_discos, 'A', 'C', 'B')
