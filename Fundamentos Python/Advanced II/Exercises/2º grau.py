import math

def delta(a, b, c):
    return b * b - 4 * a * c




print("Calculadora de 2º grau")
print("Apenas indices inteiros!")

a = int(input("Qual indice a? "))
b = int(input("Qual indice b? "))
c = int(input("Qual indice c? "))

disc = delta(a, b, c)

if disc > 0:
    
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print("As raizes são: {:.2f} e {:.2f}".format (x1, x2))
    
elif disc == 0:
    #x1 = x2
    x = (-b / (2 * a) )
    print("A raiz é: {:.2f}".format (x))

else:
    print("Nao existem raizes reais")
    
    

