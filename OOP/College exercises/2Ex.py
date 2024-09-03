'''
- Ler a cotação do dólar
- Ler um valor em dólares
- Converter esse valor para Real
- Mostrar o resultado
'''
cot_dolar = float(input("Qual a cotação atual: "))
valor_dolar = float(input("Qual valor do money: "))

valor_real = cot_dolar * valor_dolar
print(f"{valor_real:.2f} R$")