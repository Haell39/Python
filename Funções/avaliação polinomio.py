def avaliar_polinomio(coeficientes, x):
    """
    Avalia um polinômio para um dado valor de x.
    coeficientes: lista de coeficientes [a0, a1, a2, ..., an]
                  onde a0 + a1*x + a2*x^2 + ... + an*x^n
    x: valor para o qual o polinômio será avaliado
    Retorna o valor do polinômio em x.
    """
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** i)
    return resultado

# Testando a função avaliar_polinomio
coeficientes = [1, 0, 2]  # Representa o polinômio 1 + 0*x + 2*x^2
x = 3
valor_polinomio = avaliar_polinomio(coeficientes, x)
print(f"Polinômio avaliado em x={x}: {valor_polinomio}")  # Saída: 19


avaliar_polinomio_lambda = lambda coeficientes, x: sum(coef * (x ** i) for i, coef in enumerate(coeficientes))

# Testando a função lambda
coeficientes = [1, 0, 2]  # Representa o polinômio 1 + 0*x + 2*x^2
x = 3
valor_polinomio_lambda = avaliar_polinomio_lambda(coeficientes, x)
print(f"Polinômio avaliado em x={x} usando lambda: {valor_polinomio_lambda}")  # Saída: 19


def avaliar_polinomio_recursivo(coeficientes, x, n=None):
    """
    Avalia um polinômio para um dado valor de x usando recursão.
    coeficientes: lista de coeficientes [a0, a1, a2, ..., an]
    x: valor para o qual o polinômio será avaliado
    n: grau atual do polinômio (para controle da recursão)
    Retorna o valor do polinômio em x.
    """
    if n is None:
        n = len(coeficientes) - 1
    if n == 0:
        return coeficientes[0]
    return coeficientes[n] * (x ** n) + avaliar_polinomio_recursivo(coeficientes, x, n - 1)

# Testando a função recursiva
coeficientes = [1, 0, 2]  # Representa o polinômio 1 + 0*x + 2*x^2
x = 3
valor_polinomio_recursivo = avaliar_polinomio_recursivo(coeficientes, x)
print(f"Polinômio avaliado em x={x} usando recursão: {valor_polinomio_recursivo}")  # Saída: 19
