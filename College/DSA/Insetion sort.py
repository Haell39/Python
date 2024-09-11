def insertion_sort_simulation(arr):
    simulation = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Registra o estado antes de começar a inserção desse krai
        simulation.append(arr[:]) 
        
        # Move os elementos 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        
        # Registra o estado após a inserção
        simulation.append(arr[:]) 
        
    return simulation

# Array de caracteres pra ajeitar
array = list("RAFAELANDR")
iterations = insertion_sort_simulation(array)

# Exibição que o mayrton quer
for index, step in enumerate(iterations):
    print(f"Iteração {index + 1}: {step}")