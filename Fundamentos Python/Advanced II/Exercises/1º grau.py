

#Função para equação do grau 1:

def equacao1(a, b):
    return (-b/a)

a = float(input("Qual indice a? "))
b = float(input("Qual indice b? "))

if (a == 0):
    print("Não e uma equação do 1º grau")
else:
    x = equacao1(a, b)
    print("X = ", x)

