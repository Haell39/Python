def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Quantos termos vc quer mostrar?: "))
for i in range(n):
    print(fibo(i))