def farctocelcius(F):
    return (F - 32) * 5/9

temp_f = float(input("Digite a temperatura em Fahrenheit: "))
print(f'{farctocelcius(temp_f):.2f} C')