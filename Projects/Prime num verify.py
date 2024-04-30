def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    num = input("Enter a number (or type '0' to quit): ")
    if num == "0":
        print("Goodbye!!")
        break
    num = int(num)  # Convertendo a entrada para um número inteiro
    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number.")
