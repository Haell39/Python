def rectangle_perimeter(length: int, width: int) -> int:
    # your code here
    peri = 2 * length + 2 * width
    # peri = 2 * (length + width)
    # rectangle_perimeter = lambda a,b: a+a+b+b tambem funciona 
    return peri


print("Example:")
print(rectangle_perimeter(3, 2))

# These "asserts" are used for self-checking
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18
assert rectangle_perimeter(1, 1) == 4
assert rectangle_perimeter(1, 5) == 12
assert rectangle_perimeter(4, 1) == 10
assert rectangle_perimeter(100, 100) == 400
assert rectangle_perimeter(0.5, 2) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")