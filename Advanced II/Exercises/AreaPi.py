import math
PI = 3.14

def circlearea(raio):
    area = PI * (raio ** 2)
    return area

a = int(input("Digite o raio da circunferência: "))
print("The area of the circle is: \n")
print(circlearea(a))