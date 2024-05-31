# 1. Variáveis e Tipos de Dados
idade = 30  # Inteiro (int)
nome = "Alice"  # String (str)
altura = 1.65  # Ponto flutuante (float)
aprovado = True  # Booleano (bool)

print(type(idade))  # Imprime o tipo da variável

# 2. Operadores
soma = 5 + 3
subtracao = 10 - 2
multiplicacao = 4 * 6
divisao = 20 / 4
modulo = 17 % 3
exponenciacao = 2 ** 3

maior_que = 5 > 3
menor_que = 2 < 8
igual = 10 == 10
diferente = 5 != 3
e_logico = True and False
ou_logico = True or False
nao_logico = not True

# 3. Estruturas de Controle de Fluxo (if, elif, else)
nota = 75
if nota >= 70:
    print("Aprovado!")
elif nota >= 50:
    print("Recuperação.")
else:
    print("Reprovado.")

# 4. Estruturas de Repetição (for, while)
# for (itera sobre elementos)
for i in range(5):  # Repete 5 vezes (0 a 4)
    print(i)

# while (repete enquanto a condição for verdadeira)
contador = 0
while contador < 3:
    print("Contando:", contador)
    contador += 1

# 5. Listas, Tuplas, Conjuntos e Dicionários
frutas = ["maçã", "banana", "laranja"]  # Lista
coordenadas = (3, 5)  # Tupla (imutável)
numeros_unicos = {1, 2, 3, 3}  # Conjunto (sem repetição)
pessoa = {"nome": "João", "idade": 25}  # Dicionário

# 6. Funções e Lambdas
def saudacao(nome):
    print("Olá,", nome)

saudacao("Maria")

# Função lambda (anônima)
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10

# 7. Classes e Objetos
class Cachorro:
    def __init__(self, nome, raca):  # Construtor
        self.nome = nome
        self.raca = raca

    def latir(self):
        print("Au au!")

meu_cachorro = Cachorro("Rex", "Labrador")
meu_cachorro.latir()

# 8. Tratamento de Exceções (try, except)
try:
    resultado = 10 / 0  # Gera um erro de divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# 9. Módulos e Pacotes
import math  # Importa o módulo math

print(math.sqrt(25))  # Calcula a raiz quadrada de 25
