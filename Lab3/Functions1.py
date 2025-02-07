# 1. 
def grams_to_ounces(grams):
    return 28.3495231 * grams


# 2. 
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)


# 3. 
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None


# 4. 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))


# 5. 
from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))


# 6. 
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


# 7. 
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# 8. 
def spy_game(nums):
    pattern = [0, 0, 7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return True
    return False


# 9. 
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)


# 10. 
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


# 11. 
def is_palindrome(word):
    return word == word[::-1]


# 12. 
def histogram(lst):
    for num in lst:
        print("*" * num)


# 13. 
import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("\nTake a guess.\n"))
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break


