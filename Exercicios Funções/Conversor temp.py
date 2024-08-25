# Funções para conversão de temperaturas

# Celsius para Fahrenheit e Kelvin
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

# Fahrenheit para Celsius e Kelvin
def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# Kelvin para Celsius e Fahrenheit
def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Recebendo a entrada do usuário
while True:
    
    temperatura = float(input("Digite a temperatura: "))
    escala = input("Digite a escala (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

    # Realizando as conversões de acordo com a escala informada
    if escala == 'C':
        print(f"{temperatura}°C é igual a {celsius_para_fahrenheit(temperatura):.2f}°F e {celsius_para_kelvin(temperatura):.2f}K")
    elif escala == 'F':
        print(f"{temperatura}°F é igual a {fahrenheit_para_celsius(temperatura):.2f}°C e {fahrenheit_para_kelvin(temperatura):.2f}K")
    elif escala == 'K':
        print(f"{temperatura}K é igual a {kelvin_para_celsius(temperatura):.2f}°C e {kelvin_para_fahrenheit(temperatura):.2f}°F")
    else:
        print("Escala inválida! Use 'C' para Celsius, 'F' para Fahrenheit, ou 'K' para Kelvin.")
        
    # Verificando se o usuário deseja continuar
    resposta = input("Deseja continuar (S para sim e N para não)? ").upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        print("Encerrando programa...")
        break
    else:
        print("Resposta inválida! Use 'S' para sim e 'N' para não.")
        
