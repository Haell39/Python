# Criação de uma lista
lista = [1, 2, 3, 4, 5]
print("Lista inicial:", lista)

# Adição de elementos
lista.append(6)
print("Lista após adicionar 6:", lista)

# Inserção de elementos em uma posição específica
lista.insert(2, 2.5)
print("Lista após inserir 2.5 na posição 2:", lista)

# Remoção de elementos
lista.remove(3)
print("Lista após remover o elemento 3:", lista)

# Acesso a elementos
print("Elemento na posição 0:", lista[0])
print("Último elemento:", lista[-1])

# Comprimento da lista
print("Comprimento da lista:", len(lista))

# Iteração sobre elementos
for item in lista:
    print("Elemento:", item)
