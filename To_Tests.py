# Counting Sort used by Radix Sort with Debugging
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n  # Output array to store sorted elements
    count = [0] * 10  # Count array to store the count of digits (0 to 9)

    # Print the current array and the digit position being sorted
    print(f"\nSorting for exponent (digit place): {exp1}")
    print(f"Current array: {arr}")

    # Store the count of occurrences of each digit in count[]
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[int(index % 10)] += 1
    print(f"Count array after counting digits: {count}")

    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f"Cumulative count array: {count}")

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        print(f"Placing {arr[i]} in position {count[int(index % 10)]} of output array.")
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers
    for i in range(0, len(arr)):
        arr[i] = output[i]
    
    # Print the sorted array after this pass
    print(f"Array after sorting for exponent {exp1}: {arr}")

# Radix Sort function with Debugging
def radixSort(arr):
    # Find the maximum number to know the number of digits
    max1 = max(arr)

    # Perform counting sort for every digit. exp is 10^i where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Example array
arr = [8, 7, 5, 6, 3]

print("Original array:")
print(arr)

# Perform Radix Sort
radixSort(arr)

print("\nSorted array:")
print(arr)
