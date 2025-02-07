# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class TextProcessor:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


# 2. Define a class named Shape and its subclass Square.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# 3. Define a class named Rectangle which inherits from Shape class from task 2.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 4. Write the definition of a Point class. 
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount


# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
