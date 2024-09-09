def calcular(a, operador,b):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        return a / b
    elif operador == "%":
        return a % b
    elif operador == "**":
        return a ** b
    
a = float(input("Qual o primeiro valor? "))
operador = input("Qual operação deseja fazer: +, -, *, /, %, **? ")
b = float(input("Qual o segundo valor? "))

print(calcular(a, operador, b))


