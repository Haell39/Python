#Conversor de temperatura (Celsius, Fahrenheit) função:
def celsius_to_fahrenheit(celsius):
  return celsius * 9/5 + 32
#def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

text = int(input("Type a temperature in Celsius: "))
print(celsius_to_fahrenheit(text))