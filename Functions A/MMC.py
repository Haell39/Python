#Calculate the MMC of two numbers:
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    return (a * b) // mdc(a, b)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O MMC de {a} e {b} é {mmc(a, b)}")
print(f"O MDC de {a} e {b} é {mdc(a, b)}")