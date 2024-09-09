def decresc(a,b,c):
    if a > b and a > c and b > c:
        return a, b, c
    elif b > a and b > c and a > c:
        return b, a, c
    elif c > a and c > b and a > b:
        return c, a, b
    elif c > a and c > b and b > a:
        return c, b, a
    elif b > c and b > a and c > a:
        return b, c, a
    elif a > c and a > b and c > b:
        return a, c, b

#*outro jeito de fazer isso melhor:

# def decresc(a, b, c):
#?     return sorted([a, b, c], reverse=True)
    
#*para digitar varios valores em uma linha de codigo:
#? a, b, c = map(int, input("digite 3 valores: ").split()) 

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

print(decresc(a,b,c))
