# Python builtin functions exercises

import math
import time

# 1. Write a Python program with builtin function to multiply all the numbers in a list

Numbers = list(map(int, input("Enter the numbers separated by a space: ").split()))

Result = math.prod(Numbers)

print(Result)

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

Text = input()

Uppercase = sum(1 for char in Text if char.isupper())
Lowercase = sum(1 for char in Text if char.islower())

print(Uppercase)
print(Lowercase)

# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not

Text = input()

Palindrome = Text == Text[::-1]

print("It is a palindrome" if Palindrome else "It is not a palindrome")

# 4. Write a Python program that invoke square root function after specific milliseconds

Number = int(input())
Delay = int(input())

time.sleep(Delay / 1000)

Result = math.sqrt(Number)

print(f"Square root of {Number} after {Delay} miliseconds is {Result}")

# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true

Values = tuple(map(int, input().split()))

Result = all(Values)

print(Result)

