# Função para avaliar um polinômio
def avalia_polinomio(coeficientes, x):
    resultado = 0
    grau = len(coeficientes) - 1
    for coef in coeficientes:
        resultado += coef * (x ** grau)
        grau -= 1
    return resultado

# Lista de coeficientes para o polinômio 2x^3 + 3x^2 + x + 5
coeficientes = [2, 3, 1, 5]
x = 2
resultado = avalia_polinomio(coeficientes, x)
print(f"Polinômio avaliado em x = {x}: {resultado}")  # Saída: Polinômio avaliado em x=2: 27
