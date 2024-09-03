PI = 3.14159

def volume_lata_oleo():
    R = float(input("Qual o raio da lata? "))
    A = float(input("Qual a altura da lata? "))
    Volume = PI * R * R * A
    return Volume

result = volume_lata_oleo()
print(f'O volume da lata é de {result:.2f}cm³')

