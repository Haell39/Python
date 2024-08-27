def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  
#fução retorna o numero segundo o termo da sequencia fibbonacci
x = int(input("Qual termo vc quer descobrir?: "))
print(fibonacci(x))