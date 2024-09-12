# Simular o algoritmo de ordenação Quick Sort:

def partição(array, low, high):
    pivot = array[high]  # Choosing the pivot element
    i = low - 1  # Pointer for the greater element

    print(f"\nIniciando partição com pivot {pivot} entre {low} e {high}.")
    print(f"Estado inicial do array: {array}")

    # Traverse through all elements
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1  # Increment index of smaller element
            array[i], array[j] = array[j], array[i]  # Swap elements
            print(f"Swapping elements {array[i]} e {array[j]}: {array}")

    # Swap the pivot element to the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    print(f"Movendo o pivot {pivot} para o meio: {array}")

    return i + 1

def quickSort(array, low, high):
    if low < high:
        # Partitioning index
        pi = partição(array, low, high)
        print(f"Array após partição em {pi}: {array}")

        # Recursively apply to the left of pivot
        quickSort(array, low, pi - 1)
        # Recursively apply to the right of pivot
        quickSort(array, pi + 1, high)

data = [96, 80, 6, 40, 15, 46, 71, 31, 77, 82]
print("Array desordenado:")
print(data)

size = len(data)
quickSort(data, 0, size - 1)

print("\nSorted array in Ascending Order:")
print(data)
