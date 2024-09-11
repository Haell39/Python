def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

U = input("Enter the numbers to be sorted: ")
U = list(map(int, U.split()))
print(f'Ordered List = {bubble_sort(U)}')