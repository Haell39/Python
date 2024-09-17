# Count Sort for Numerical Data with Debugging
def countSortNumbers(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count and output arrays
    count = [0] * range_of_elements
    output = [0] * len(arr)

    print(f"Initial array: {arr}")
    print(f"Range of elements: {range_of_elements}")
    print(f"Count array initialized: {count}\n")

    # Store the count of each element in the count array
    for num in arr:
        count[num - min_val] += 1
        print(f"Counting element {num}: {count}")

    # Store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        print(f"Cumulative count at index {i}: {count}")

    print("\nCumulative count array after counting: ", count)

    # Place the elements in output array in sorted order
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
        print(f"Placing element {num} in sorted order: {output}")
        print(f"Updated count array: {count}")

    # Copy sorted elements to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

    print("\nFinal sorted array: ", arr)
    return arr

# Example for sorting numbers
array = [4,6,6,2,0,3,5,1,1,2]
sorted_array = countSortNumbers(array)
print("\nSorted number array is:", sorted_array)
