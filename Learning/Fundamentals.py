# Importação de bibliotecas
import math

# Variáveis e tipos de dados
nome = "João"  # String
idade = 30  # Inteiro
altura = 1.75  # Float
ativo = True  # Booleano

# Sintaxe básica
print("Olá, mundo!")  # Impressão de texto
print(f"Meu nome é {nome} e tenho {idade} anos.")  # F-strings

# Condicionais
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Loops
for i in range(5):
    print(i)

# Funções
def soma(a, b):
    return a + b

print(soma(2, 3))  # Chamada de função

# Listas e arrays
frutas = ["maçã", "banana", "uva"]
print(frutas[0])  # Acessando elementos de uma lista

# Dicionários
pessoa = {"nome": "João", "idade": 30}
print(pessoa["nome"])  # Acessando elementos de um dicionário

# Classes e objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("João", 30)
pessoa.apresentar()  # Chamada de método

# Módulos e bibliotecas
import math
print(math.pi)  # Acessando uma constante do módulo math

# Erros e exceções
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# Comentários
# Este é um comentário de uma linha
"""
Este é um comentário de múltiplas linhas
que pode ser utilizado para explicar o código
"""