def bubble_sort_simulation(arr):
    simulation = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Registra o estado antes da possível troca
            simulation.append(arr[:]) 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return simulation

array = [65, -32, 79, -22, 40, -68, -81, -21, 95, -46]
iterations = bubble_sort_simulation(array)
for step in iterations:
    print(step)