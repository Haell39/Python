# Use uma compreensão de lista para criar uma lista contendo os quadrados dos números de 1 a 10. Em seguida, imprima a lista resultante

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in range(1, 11)]


print(squares)