def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    
f = int(input("Choose a factorial: "))
print(f"The factorial of the choosen number is: {factorial(f)}")