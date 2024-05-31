# Função lambda para adicionar dois números
soma = lambda x, y: x + y

print(f"Soma usando lambda: {soma(2, 3)}")  # Saída: 5

# Uso de lambda com `filter` para filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números pares usando lambda: {numeros_pares}")  # Saída: [2, 4, 6]
