def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


a = int(input("Choose a factorial: "))

print(factorial(a))
