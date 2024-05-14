# return = statement used to end a function
# and send a value(result) back to the caller

def add(a, b):
    z = a + b
    return z

# tambem poderia fazer:
# def add(a, b):
#     return a + b #Isoo tbm funcionaria igual

def sub(a, b):
    z = a - b
    return z

def mult(a, b):
    z = a * b
    return z

def divid(a, b):
    z = a / b
    return z

def rest(a, b):
    z = a % b
    return z

def divid_inteiro(a, b):
    z = a // b
    return z






print(add(5,7))
print(sub(5,7))
print(divid(5,7))
print(mult(5,7))
print(rest(5,7))
print(divid_inteiro(124,7))
