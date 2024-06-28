#Crie um dicionário que mapeia nomes de frutas para suas cores. Em seguida, imprima a cor de uma fruta específica fornecida pelo usuário.

My_Fruits = {
    
    'Apple' : 'Red',
    'Banana' : 'Yellow',
    'Orange' : 'Orange',
    'Grape' : 'Purple',
    'Strawberry' : 'Red',
    'Peach' : 'Yellow',
    'Cherry' : 'Red',
}

while True:
    Fruits = input("Type the name of the fruit: ")

    if Fruits in My_Fruits:
        print(f"The color of {Fruits} is {My_Fruits[Fruits]}") 
    else:
        print(f"{Fruits} is not in the list")
        break



