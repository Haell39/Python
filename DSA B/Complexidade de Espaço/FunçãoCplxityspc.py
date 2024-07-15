#Caso Prático: Implementação de uma Função com Diferentes Complexidades de Espaço

#Versão 1: Complexidade de Espaço O(1)

def sum_elements_constant_space(arr):
    total_sum = 0  # Espaço adicional fixo para a variável total_sum
    for num in arr:
        total_sum += num
    return total_sum

# Chamada de exemplo
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(sum_elements_constant_space(arr))  # Saída: 36


#Versão 2: Complexidade de Espaço O(n)


def sum_elements_linear_space(arr):
    partial_sums = []  # Espaço adicional proporcional ao tamanho da lista de entrada
    for num in arr:
        if not partial_sums:
            partial_sums.append(num)
        else:
            partial_sums.append(partial_sums[-1] + num)
    return partial_sums[-1]

# Chamada de exemplo
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(sum_elements_linear_space(arr))  # Saída: 36


#--------------------------------------------------------------

#Conclusão: A complexidade de espaço é uma métrica importante para avaliar a eficiência de um algoritmo em termos de uso de memória. Um bom entendimento da complexidade de espaço ajuda a projetar algoritmos mais eficientes, especialmente em ambientes com recursos limitados.






