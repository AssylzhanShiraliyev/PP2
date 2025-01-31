#Python Lists

mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])

#List items cannot be removed after the list has been created. This statement is false.

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

#Python Access Lists

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Python Change Lists

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

#Python Add List Items

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

#Python Remove List Items

#What is a List method for removing list items? pop().

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)

fruits = ['apple', 'banana', 'cherry']
fruits.clear()

#Python Loop Lists

#What is a correct syntax for looping through the items of a list? for x in ['apple', 'banana', 'cherry']: print(x)

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

#What is a correct syntax for looping through the items of a list? [print(x) for x in ['apple', 'banana', 'cherry']]

#Python List Comprehension

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana'] #What will be the value of newlist? ['banana']

fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits] #What will be the value of newlist? ['apple', 'apple', 'apple']

#Python Sort Lists

#What is a correct syntax for sorting a list? mylist.sort()

#What is a correct syntax for reversing the current order of a list? mylist.reverse()

#What is a correct syntax for sorting a list descending? mylist.sort(reverse = True)

#Python Copy Lists

#What is a correct syntax for making a copy of a list? list2 = list1.copy()

#What is a correct syntax for making a copy of a list? list2 = list(list1)

#What is a correct syntax for making a copy of a list? list2 = list1[:]

#Python Join Lists

#What is a correct syntax for joining list1 and list2 into list3? list3 = list1 + list2

#What is a correct syntax for adding elements from list2 into list1? list1.extend(list2)

list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x) #What will be the value of list1? ['a', 'b', 'c', 1, 2, 3]