# Merge function to merge two subarrays
def merge(arr, left, mid, right):
    # Calculate the lengths of two subarrays to be merged
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temporary arrays back into arr[left..right]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# MergeSort function
def mergeSort(arr, left, right):
    if left < right:
        # Calculate mid point to divide the array
        mid = left + (right - left) // 2

        # Call mergeSort on the first half
        mergeSort(arr, left, mid)

        # Call mergeSort on the second half
        mergeSort(arr, mid + 1, right)

        # Merge the two halves
        merge(arr, left, mid, right)

# Driver code
arr = [81, 47, -20, 1, 3, -4, 15, -90, 0, -77]
n = len(arr)
print("Original array is: ")
for i in range(n):
    print("%d" % arr[i], end=" ")

# Call mergeSort
mergeSort(arr, 0, n-1)
print("\n\nSorted array is: ")
for i in range(n):
    print("%d" % arr[i], end=" ")
