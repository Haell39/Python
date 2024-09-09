#Programa para verificar o MMC de dois números:

def mmc(a,b):
    mmc = 1
    for i in range(1, a*b+1):
        if i % a == 0 and i % b == 0:
            mmc = i
            break
    return mmc

a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

print("MMC = {}".format(mmc(a,b)))