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
print(car)  #Now theres only brand


