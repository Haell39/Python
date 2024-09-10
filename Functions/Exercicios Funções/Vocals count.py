#Contador de vogais:

def count_vowels(sentence):
    c = 0
    for char in sentence:
        if char in "aeiouAEIOU":
            c += 1
    return c

print("Digite uma frase:")
sentence = input()
print(f'O numero de vogais nesta frase é: {count_vowels(sentence)}')