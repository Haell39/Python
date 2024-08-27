#Callculate the average of the numbers in a list:
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

list = [1, 2, 3, 4, 5]
print(calculate_average(list))