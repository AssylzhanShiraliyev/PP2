def grams_to_ounces(grams):
    return 28.3495231 * grams

def is_palindrome(word):
    return word == word[::-1]

def sphere_volume(radius):
    import math
    return (4 / 3) * math.pi * (radius ** 3)
