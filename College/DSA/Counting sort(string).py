def countSort(arr):
    # Initialize output and count arrays
    output = [0 for _ in range(len(arr))]
    count = [0 for _ in range(256)]  # 256 for ASCII character set

    # Store the count of each character
    for char in arr:
        count[ord(char)] += 1

    # Store the cumulative count
    for i in range(1, 256):
        count[i] += count[i - 1]

    # Place the characters in output array in sorted order
    for i in range(len(arr) - 1, -1, -1):
        char = arr[i]
        output[count[ord(char)] - 1] = char
        count[ord(char)] -= 1

    # Convert the output list to a string and return
    return "".join(output)

# Example for sorting a string
arr = "RAFAELANDRADE"
ans = countSort(arr)
print("Sorted character array is: %s" % ans)