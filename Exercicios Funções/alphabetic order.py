# Write a Python program to sort a string lexicographically.

def order(frase):
    return ' '.join(sorted(frase.split(), key=str.lower))

frase = input("Type a sentence or words: ")
print(order(frase))


