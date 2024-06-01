print("Iniciando programa")


while True:
    a = int(input("Digite um numero, ou digite 0 para encerrar: "))
    if a == 0:
        print("ending program")
        break
    elif a % 2 == 0:
        print("Even")
    else:
        print("odd")
