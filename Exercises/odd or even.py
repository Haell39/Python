print("Type an integer")
a = int(input("Digite stop se quiser sair: "))
while True:
    if a == 0:
        print("Goodbye!!")
        break
    if a % 2 == 0:
        print("Even")
    else:
        print("odd")
