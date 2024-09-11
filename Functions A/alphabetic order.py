def ordenar_palavras(frase):
    palavras = frase.split()  # divide a string em uma lista de palavras
    palavras.sort(key=str.lower)  # ordena a lista de palavras em ordem alfabética
    return ' '.join(palavras)  # junta as palavras novamente em uma string

# Exemplo de uso:
frase =input("Say your text:")
print(f'Palavras ordenadas: {ordenar_palavras(frase)}')

