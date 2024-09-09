def sum_elements_constant_space(arr):
    total_sum = 0  # Espaço adicional fixo para a variável total_sum
    for num in arr:
        total_sum += num
    return total_sum

# Chamada de exemplo
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(sum_elements_constant_space(arr))  # Saída: 36
