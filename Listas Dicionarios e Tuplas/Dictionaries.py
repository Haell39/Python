# Python Dictionaries

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud',
}

#Set key, value using subscript operator

my_cat['age_years'] = 2
print(my_cat)

#Get value using subscript operator

print(my_cat['color'])

#Values()
#The values() method gets the values of the dictionary:

pet = {'color': 'red', 'age': 42}
for value in pet.values():
    print(value)  #This way the code will gets only the values from the dictionary >> red 42

#keys

for key in pet.keys():
    print(key)  #This way the code will gets only the keys from the dictionary >> color age


#items

for item in pet.items():
    print(item)  #This way the code will gets the keys and values from the dictionary(The items) >> color red age 42


#Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.

for key, value in pet.items():
    print(f'key: {key} value: {value}') 


#Get()

#The get() method returns the value of an item with the given key. If the key doesn’t exist, it returns None:


wife = {'name': 'Rose', 'age': 33}

print(f'\nMy wife name is {wife.get("name")}')

print(f'She is {wife.get("age")}')

print(f'She is deeply in lover with {wife.get("husband", "her Lover")}') #If the key doesn’t exist, it returns None, but You can also change the default None value to one of your choice:


#Adding items with setdefault()

#It’s possible to add an item to a dictionary in this way:

if 'wife_hair' not in wife:
    wife['has_hair'] = True
print(wife,"\n")

#now using setdefault()

husband = {'name': 'John', 'age': 45}
husband.setdefault('has_hair', True)
print(husband,"\n")


#Removing Items

car = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car.pop('year')
print(car)

#The popitem() method removes the last item in a dictionary and returns it.

car.popitem()
print(car,"\n")  #Now theres only brand


#del()
# The del() method removes an item based on a given key.

book = {'author': 'Alice', 'title': 'Alice in Wonderland',}

del book['title']
print(book ,"\n")


#Clear --> Removes all items from the dictionary

motobike = {'brand': 'Yamaha', 'model': 'YZF-R1', 'year': 2022}
motobike.clear()
print(motobike ,"\n")


#Cheking keys in dictionary

person = {'name': 'John', 'age': 30, 'city': 'New York'}

a = 'name' in person.keys()
b = 'John' in person.values()
c = 'height' in person.keys()

print("Checking keys in dictionary")
print(a)
print(b)
print(c ,"\n")


person2 = {'name': 'rael', 'age': 24}
q = 'John' in person2.values()
t = 24 in person2.values()

print("Checking values in dictionary")
print(q)
print(t ,"\n")


#Pretty Print
print("Pretty Print")
import pprint
wife2 = {'name': 'Rose', 'age': 33, 'has_hair': True, 'hair_color': 'brown', 'height': 1.6, 'eye_color': 'brown'}
pprint.pprint(wife2)



