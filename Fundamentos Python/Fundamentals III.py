# Lambda functions
# Uma função lambda é uma função que não tem nome
# Ela é definida usando a palavra-chave lambda, seguida de uma expressão
# O exemplo abaixo define uma função lambda que eleva um número à potência de 2
squares = list(map(lambda x: x ** 2, range(5)))
print(squares)  # [0, 1, 4, 9, 16]

# Geradores
# Um gerador é uma função que gera valores, mas não os calcula imediatamente
# Em vez disso, o gerador produz os valores quando são solicitados
# O exemplo abaixo define uma função geradora que gera a sequência de Fibonacci
def fibonacci():
    a, b = 0, 1  # valores iniciais da sequência
    while True:  # loop infinito
        yield a  # gera o valor atual da sequência
        a, b = b, a + b  # avança para o próximo valor da sequência

fib = fibonacci()  # cria um gerador
for _ in range(10):  # imprime os primeiros 10 valores da sequência
    print(next(fib))

# Itertools
# A biblioteca itertools é uma coleção de funções que trabalham com iteradores
# Um iterador é um objeto que gera valores, mas não os calcula imediatamente
# O exemplo abaixo usa a função cycle para criar um iterador que repete
# a lista de frutas infinitamente
import itertools
fruits = ["apple", "banana", "cherry"]
for fruit in itertools.cycle(fruits):
    print(fruit)
    if fruit == "cherry":  # para o loop quando a fruta é "cherry"
        break

# Regular Expressions
# As expressões regulares são usadas para procurar por padrões em textos
# O exemplo abaixo usa a função search da biblioteca re para procurar
# um número de telefone no texto
import re
text = "Hello, my phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # expressão regular para procurar números de telefone
match = re.search(pattern, text)
print(match.group())  # 123-456-7890

# Try-except blocks
# O bloco try-except é usado para capturar erros
# O bloco try executa um código, e o bloco except é executado se um erro for
# gerado durante a execução do try
# O exemplo abaixo tenta dividir por zero, mas captura o erro
# e imprime uma mensagem de erro
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# Context managers
# Um context manager é uma função que é executada automaticamente
# antes e depois de um bloco de código
# O exemplo abaixo abre um arquivo para escrita, escreve algo nele,
# e fecha o arquivo automaticamente
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Decorators
# Um decorator é uma função que é aplicada a outra função
# para modificar seu comportamento
# O exemplo abaixo define um decorator que imprime uma mensagem
# antes e depois de uma função ser chamada
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

# O decorator é aplicado à função add
@my_decorator
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
