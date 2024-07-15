def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Chamada de exemplo
print(fibonacci(5))  # Saída: 5
