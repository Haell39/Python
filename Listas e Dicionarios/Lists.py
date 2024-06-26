#Basic exemple:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print(num)
    
#To Modify list: 

double_num = [num * 2 for num in nums]

print(double_num)


#Filtrar lista:

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

#Elevar cada num ao quadrado:

square_nums = [num ** 2 for num in nums]
print(square_nums)