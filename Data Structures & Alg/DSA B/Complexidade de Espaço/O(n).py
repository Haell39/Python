def duplicate_elements(arr):
    duplicated_list = []  # Espaço adicional para a lista duplicada
    for num in arr:
        duplicated_list.append(num * 2)
    return duplicated_list

# Chamada de exemplo
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(duplicate_elements(arr))  # Saída: [6, 2, 8, 2, 10, 18, 4, 12, 10]
