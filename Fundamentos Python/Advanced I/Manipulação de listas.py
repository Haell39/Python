# Exemplo básico de iteração sobre uma lista e manipulação
numeros = [1, 2, 3, 4, 5]

# Iterar sobre a lista e imprimir cada número
for numero in numeros:
    print(f"Número: {numero}")

# Multiplicar cada número por 2 e criar uma nova lista
numeros_dobrados = [numero * 2 for numero in numeros]
print(f"Números dobrados: {numeros_dobrados}")

# Filtrar números pares da lista
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(f"Números pares: {numeros_pares}")
