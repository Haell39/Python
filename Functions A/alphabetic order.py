def ordenar_palavras(frase):
    palavras = frase.split()  # divide a string em uma lista de palavras
    palavras.sort()  # ordena a lista de palavras em ordem alfabética
    return ' '.join(palavras)  # junta as palavras novamente em uma string

# Exemplo de uso:
frase =input("Say your text:")
print(ordenar_palavras(frase))  