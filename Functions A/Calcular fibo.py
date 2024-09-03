# Calcular fibonacci até determinado termo:

def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib1 = 0
        fib2 = 1
        sequencia = [0, 1]
        for i in range(2, n + 1):
            fib = fib1 + fib2
            sequencia.append(fib)
            fib1 = fib2
            fib2 = fib
        return sequencia

# Mostrar fibonacci até determinado termo:

n = int(input("Até qual termo vc quer descobrir?: "))
print(fibonacci(n))