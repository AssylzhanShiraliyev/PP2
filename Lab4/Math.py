# Python Math library

import math

# 1. Write a Python program to convert degree to radian.

Degree = float(input("Input degree: "))

Radian = Degree * math.pi / 180

print("Output radian:", round(Radian, 6))

# 2. Write a Python program to calculate the area of a trapezoid.

Height = float(input("Height: "))
First = float(input("Base, first value: "))
Second = float(input("Base, second value: "))

Area = Height * (First + Second) / 2

print("Expected Output:", round(Area, 2))

# 3. Write a Python program to calculate the area of regular polygon.

Number = int(input("Input number of sides: "))
Length = float(input("Input the length of a side: "))

Area = (Number * Length ** 2) / (4 * math.tan(math.pi / Number))
Result = round(Area, 2)

print("The area of the polygon is:", int(Result) if Result.is_integer() else Result)

# 4. Write a Python program to calculate the area of a parallelogram.

Length = float(input("Length of base: "))
Height = float(input("Height of parallelogram: "))

Answer = Length * Height

print("Expected Output:", round(Answer, 2))

