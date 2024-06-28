# Taken from mission Empty Function

# write your code here
def func(arg):
    return arg


print("Example:")
print(func(3)) # como minha função tem como argumento arg e retorna arg(o proprio argumento) nessa chamada da função func como o argumento é 3, logo retorna 3!!

# print(func(3)) calls the func function with the argument 3. The function returns the value 3 (which is the argument itself), and print then displays that value (3) on the console.
# Key Point: The line print(func(3)) is what actually prints 3. The function func doesn't modify the argument arg, it just returns it.

# These "asserts" are used for self-checking
assert func(3) == 3 # retorna 3
assert func("string") == "string" # retorna string
assert func(True) == True # retorna true 

print("The mission is done! Click 'Check Solution' to earn rewards!")
