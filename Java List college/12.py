#Modulo de um numero:

def modulus(x):
    if x>0:
        return x
    else:
        return -x
    

#chamada da funcao:
num = int(input("Enter a number: "))

print(f'O modulo de {num} é {modulus(num)}')