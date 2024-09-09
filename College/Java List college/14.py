def diferenca(x,y):
    if x > y:
        return x - y
    else:
        return y - x
    
a = int(input("Qual o primeiro valor?: "))
b = int(input("Qual o segundo valor?: "))

print(f'A diferença entre {a} e {b} é igual a {diferenca(a,b)}')