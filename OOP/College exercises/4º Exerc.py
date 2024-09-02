def calc_values(A, B, C, D):
    """Calculate the sum and multiplication of 4 values"""
    sums = [A + B, A + C, A + D, B + C, B + D, C + D]
    mults = [A * B, A * C, A * D, B * C, B * D, C * D]
    return sums, mults


print("Digite 4 valores numéricos:")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("A: "))
D = int(input("D: "))

sums, mults = calc_values(A, B, C, D)

print(f"Adições: {', '.join(map(str, sums))}")
print(f"Multiplicação: {', '.join(map(str, mults))}")


'''
#* Other way without function:
print("Digite 4 valores numéricos:")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("A: "))
D = int(input("D: "))

sums, mults = calc_values(A, B, C, D)
#Adições:

print(f"Adições: {', '.join(map(str, sums))}")
print(f"Multiplicação: {', '.join(map(str, mults))}")
sumAB = A + B
sumAC = A + C
sumAD = A + D

sumBC = B + C
sumBD = B + D

sumCD = C + D

print(f"Adições: {sumAB}, {sumAC}, {sumAD}, {sumBC}, {sumBD}, {sumCD}")


#Multiplicação:

multAB = A * B
multAC = A * C
multAD = A * D

multBC = B * C
multBD = B * D

multCD = C * D

print(f"Multiplicação: {multAB}, {multAC}, {multAD}, {multBC}, {multBD}, {multCD}")


<<<<<<<  94c11324-4114-4755-881f-774af1973613  >>>>>>>

'''