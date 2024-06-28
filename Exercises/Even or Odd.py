#Crie um programa que verifica se um número é par ou ímpar usando operadores aritméticos. O programa deve solicitar um número ao usuário e imprimir se o número é par ou ímpar.


while True:
    x = input("Type a number (or 'stop' to quit): ")
    if x.lower() == 'stop': # .lower transforma o valor em minusculo para ignorar caso de letras maiusculas
        print("Ending program...")
        break
    x = int(x)
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is not even (Odd)")
