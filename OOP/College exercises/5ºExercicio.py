# automovel faz 12km por litro

def calcular_consumo(tempo_gasto, velocidade_media):
    distancia_percorrida = tempo_gasto * velocidade_media
    consumo = distancia_percorrida / 12
    return consumo

tempo_gasto = int(input("digite o tempo gasto: "))
velocidade_media = int(input("digite a velocidade media: "))
consumo = calcular_consumo(tempo_gasto, velocidade_media)
distancia_percorrida = tempo_gasto * velocidade_media

# imprime o resultado
print(f"consumo = {consumo:.2f} l")
print(f"distancia_percorrida = {distancia_percorrida:.2f} km")

