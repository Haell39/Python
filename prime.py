print("Verify if a number is prime or not")
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
stop = False
while not stop:
    num = int(input("Enter a number (type 'stop' to exit): "))
    if num == 0 or num == 'stop':
        stop = True
        break
    if is_prime(num):
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')


