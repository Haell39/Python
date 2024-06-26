#definir uma função:

def saudação(nome):
    return f'Olá, {nome}!' + ' ' + 'Bom dia!'

#chamando

mensagem = saudação("Rael")
print(mensagem)

mensagem = saudação("Elan")
print(mensagem)

#Multiplos args:

def soma(a, b):
    return a + b

result = soma(4,7)
print(result)


#* Função com valores padrao:

def saudacao(nome="mundo"):
    return f"Olá, {nome}!"

print(saudacao())
print(saudacao("Rael"))

#? Função lambda:

soma = lambda x, y: x + y
print(soma(2, 3))

#* Uso de lambda com `filter`

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)


#? Função recursiva:

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1) #*essa formula faz o calculo do fatorial recursivamente da seguinte maneira: n! = n * (n-1).(n-2).(n-3)...

print(fatorial(5))
print(fatorial(7))
