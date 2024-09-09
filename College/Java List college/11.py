x = float(input("Enter a number: "))
y = float(input("Enter another number: ")) 

def swap(a,b):
    return b,a

#Printing the values
print("A = ",x)
print("B = ",y)

#Changing the values
print("Swapping...")

#Printing the values changed
x,y = swap(x,y)
print("A = ",x)
print("B = ",y)

