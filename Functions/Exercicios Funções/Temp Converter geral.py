# Conversor de temperatura Celsius, Fahrenheit e Kelvin

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Parte para o usuário escolher a conversão
conversions = {
    "1": ("Celsius para Fahrenheit", celsius_to_fahrenheit),
    "2": ("Celsius para Kelvin", celsius_to_kelvin),
    "3": ("Fahrenheit para Celsius", fahrenheit_to_celsius),
    "4": ("Fahrenheit para Kelvin", fahrenheit_to_kelvin),
    "5": ("Kelvin para Celsius", kelvin_to_celsius),
    "6": ("Kelvin para Fahrenheit", kelvin_to_fahrenheit)
}

print("Escolha a conversão que deseja fazer:")
for key, (description, _) in conversions.items():
    print(f"{key} - {description}")

choice = input("Digite o número da conversão que deseja fazer: ")

# Parte para o usuário digitar a temperatura
if choice in conversions:
    description, func = conversions[choice]
    if "Celsius" in description:
        temp = float(input("Digite a temperatura em Celsius: "))
    elif "Fahrenheit" in description:
        temp = float(input("Digite a temperatura em Fahrenheit: "))
    else:
        temp = float(input("Digite a temperatura em Kelvin: "))
    print(func(temp))
else:
    print("Opção inválida!")