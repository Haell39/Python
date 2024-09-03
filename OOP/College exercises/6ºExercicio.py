#Celsius para Fahrenheit:

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 #* or return celsius * 1.8 + 32 #* or return celsius * 9/5 + 32(without parentesis)

temp_c = float(input("Digite a temperatura em Celsius: "))
print(f'{celsius_to_fahrenheit(temp_c):.2f} F')
