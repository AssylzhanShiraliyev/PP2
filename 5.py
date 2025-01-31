#Python Dictionaries

#Which one of these is a dictionary? x = {'type' : 'fruit', 'name' : 'banana'}

#Dictionary items cannot be removed after the dictionary has been created. False

#A dictionary cannot have two keys with the same name. True

x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

#Python Access Dictionaries

#You can access item values by referring to the key name. True

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])

#Python Change Dictionaries

#Consider the following code: x = {'type' : 'fruit', 'name' : 'banana'} What is a correct syntax for changing the type from fruit to berry? x['type'] = 'berry'

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Consider the following code: x = {'type' : 'fruit', 'name' : 'banana'} What is a correct syntax for changing the name from banana to apple? x.update({'name': 'apple'})

#Python Add Dictionary Items

#Which one of these dictionary methods can be used to add items to a dictionary? update()

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' : 'green'})

#Python Remove Dictionary Items

#What is a dictionary method for removing an item from a dictionary? pop()

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']

#Python Loop Dictionaries

#What is a correct syntax for looping through the values of this dictionary: x = {'type' : 'fruit', 'name' : 'apple'}? for y in x.values(): print(y)

#What is a correct syntax for looping through the keys AND values of this dictionary: x = {'type' : 'fruit', 'name' : 'apple'}? for y, z in x.items(): print(y, z)

myset = {'apple', 'banana', 'cherry'}
for x in myset:
    print(x)

#What is a correct syntax for looping through the keys of this dictionary: x = {'type' : 'fruit', 'name' : 'apple'}? for y in x.keys(): print(y)

#Python Copy Dictionaries

#What is a correct syntax for making a copy of this dictionary: x = {'type' : 'fruit', 'name' : 'apple'}? y = x.copy()

#One of these codes is NOT a correct way of making a copy of a dictionary named x, which one: y = x.duplicate()

#Copied dictionaries will not be able to change its item values. False

#Python Nested Dictionaries

#Consider this syntax: a = {'name' : 'John', 'age' : '20'} b = {'name' : 'May', 'age' : '23'} customers = {'c1' : a, 'c2' : b} what will be a correct syntax for printing the name 'May'? print(customers['c2']['name'])

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

#A dictionary can only have one level of nested dictionaries. False

