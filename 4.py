#Python Tuples

#Which one of these is a tuple? thistuple = ('apple', 'banana', 'cherry')

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Tuple items cannot be removed after the tuple has been created. True.

#Python Access Tuples

#You can access tuple items by referring to the index number, but what is the index number of the first item? 0

fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Python Update Tuples

#You cannot change the items of a tuple, but there are workarounds. Which of the following suggestion will work? Convert tuple into a list, change item, convert back into a tuple.

#Which is a correct syntax to delete a tuple? del mytuple

#You are allowed to add a tuple to an existing tuple. True.

#Python Unpack Tuples

fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)

#Python Loop Tuples

#What is a correct syntax for looping through the items of a tuple? for x in ('apple', 'banana', 'cherry'): print(x)

mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1

thistuple = ("apple", "banana", "cherry")
for i in range (len(thistuple)):
    print(thistuple[i])

#Python Join Tuples

#What is a correct syntax for joining tuple1 and tuple2 into tuple3? tuple3 = tuple1 + tuple2

#What is a legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)? tuple1 = (1,2,3) tuple1 = tuple1 * 2

tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1 #What will be the value of tuple3? (1, 2, 3, 'a', 'b', 'c')

#Python Sets

#Which one of these is a set? myset = {'apple', 'banana', 'cherry'}

#Set items cannot be removed after the set has been created. False

#A set cannot have two items with the same value. True

fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))

#Python Access Sets

#True or False. You can access set items by referring to the index. False

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)

#Python Add Set Items

#What is a correct syntax for adding items to a set? add()

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Python Remove Set Items

#What is a correct syntax for removing an item from a set? remove()

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

fruits = {'apple', 'banana', 'cherry'}
fruits.clear()

#Python Loop Sets

#What is a correct syntax for looping through the items of a set? for x in {'apple', 'banana', 'cherry'}: print(x)

myset = {'apple', 'banana', 'cherry'}
for x in myset:
    print(x)

#Sets are unordered, so when you loop through the items, the order will be totally random. True

#Python Join Sets

#What is a correct syntax for joining set1 and set2 into set3? set3 = set1.union(set2)

#What is a correct syntax for joining multiple sets into one new set called set5? set5 = set1 | set2 | set3 | set4

#There are many ways to join sets in Python. Which one of the following methods keeps ONLY the duplicates? 
