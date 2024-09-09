print("\nLoop normal: ")

for x in range(0, 10):
    print(x)
    
print("\nLoop com argumento: ")

for y in range(0, 22, +3):
    print(y)
    
print("\nLoop negativo: ")

for z in range(10, 0, -2):
    print(z)

print("\nLoop reversed: ")

for i in reversed(range(0, 10)):
    print(i)
    
print("\nLoop reversed com argumento: ")

for j in reversed(range(0, 22, 3)):
    print(j)
    
print("\nLoop reversed negativo: ")
    
for rneg in reversed(range(10, 0, -2)):
    print(rneg)
    
print("\niterate over a string: ")

CreditCard = "1234-5678-9012-3456"
for cred in CreditCard:
    print(cred)
    
print("\nContinue and Break: ")

for x in range(0, 15):
    if x == 5:
        continue
    if x == 9:
        break
    print(x)

