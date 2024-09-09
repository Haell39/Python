# Define a function named `mult_two`
def mult_two(a: int, b: int) -> int:

  # This line indicates that the function takes two arguments, both of type integer (`int`)
  # and it will return an integer (`-> int`)
  # - `a`: The first number to be multiplied (integer)
  # - `b`: The second number to be multiplied (integer)

  # Multiply the two arguments (`a` and `b`) using the multiplication operator (`*`)
  # and store the result in a variable named `product` (although not strictly necessary here)
  product = a * b

  # Return the calculated product from the function
  return product

# Print a message as an example
print("Example")

# Call the `mult_two` function with arguments 1 and 2, and store the returned value in `result`
result = mult_two(1, 2)

# Print the result of calling the function
print(result)

# Self-checking assertions (optional) - These lines verify the function's correctness
assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

# Print a completion message
print("The first mission is done! Click 'Check' to earn cool rewards!")
