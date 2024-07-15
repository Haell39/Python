# Implementação do Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Testando o Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array original:", arr)
sorted_arr = bubble_sort(arr)
print("Array ordenado:", sorted_arr)
