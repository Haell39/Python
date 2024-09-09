# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Testar a função recursiva
numero = 5
resultado = fatorial(numero)
print(f"Fatorial de {numero}: {resultado}")  # Saída: Fatorial de 5: 120
