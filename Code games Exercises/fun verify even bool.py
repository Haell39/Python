def is_even(num: int) -> bool:
##This line of code defines a function named `is_even` that takes an integer `num` as an argument and returns a boolean value. The `num` parameter is annotated with the `int` type hint, which means that the function expects `num` to be an integer. The `-> bool` part of the function signature indicates that the function will return a boolean value.
    #In other words, this line of code is defining a function that checks if a given number is even.
    
#//* The symbol -> indicates that the function will return a certain type of value. In this case, the function will return a boolean value. */


  """
  Checks if a number is even.

  Args:
      num: The number to check (integer).

  Returns:
      True if the number is even, False otherwise.
  """

  # Check if the remainder after dividing by 2 is 0 (even number)
  if num % 2 == 0:
      return True  # Return True if even
  else:
      return False  # Return False if odd

# Example usage
print("Example:")
print(is_even(2))  # Output: True

# Self-checking assertions (optional)
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
