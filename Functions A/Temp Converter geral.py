# conversor de temperatura Celsius Faherenheit e Keivin:

#C -> F:
def celsius_to_fahrenheit(celsius):
  return celsius * 9/5 + 32
#C -> K:
def celsius_to_kelvin(celsius):
  return celsius + 273.15
#F -> C:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9
#F -> K:
def fahrenheit_to_kelvin(fahrenheit):
  return (fahrenheit - 32) * 5/9 + 273.15
#K -> C:
def kelvin_to_celsius(kelvin):
  return kelvin - 273.15
#K -> F:
def kelvin_to_fahrenheit(kelvin):
  return (kelvin - 273.15) * 9/5 + 32

#Parte para o usuario escolher a conversão:
print("Escolha a conversão que deseja fazer:")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

choice = input("Digite o número da conversão que deseja fazer: ")

#Parte para o usuario digitar a temperatura:
if choice == "1":
  celsius = float(input("Digite a temperatura em Celsius: "))
  print(celsius_to_fahrenheit(celsius))
  
if choice == "2":
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(celsius_to_kelvin(celsius))

if choice == "3":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(fahrenheit_to_celsius(fahrenheit))

if choice == "4":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print(fahrenheit_to_kelvin(fahrenheit))

if choice == "5":
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    print(kelvin_to_celsius(kelvin))

if choice == "6":
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    print(kelvin_to_fahrenheit(kelvin))


