def sumsequence():
    previous = 0
    for atual in range(10):
        result = previous + atual
        print(f"{previous} + {atual} = {result}")
        previous = atual


print(sumsequence())