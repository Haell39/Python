# Função para calcular a média aritmética de uma lista de números
def calcular_media(numeros):
    # Somando os números e dividindo pela quantidade de elementos
    media = sum(numeros) / len(numeros)
    return media

# Recebendo a entrada do usuário
entrada = input("Digite uma lista de números separados por espaços: ")

# Convertendo a entrada para uma lista de números
numeros = list(map(float, entrada.split()))

# Calculando e exibindo a média aritmética
media = calcular_media(numeros)
print(f"A média aritmética é: {media:.2f}")
