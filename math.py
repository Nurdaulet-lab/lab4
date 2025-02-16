from math import radians

degree = float(input("Input degree: "))
radian = radians(degree)

print("Output radian:", radian)

#esep2

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

# esep 3

from math import tan, pi

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * tan(pi / n))
print("The area of the polygon is:", area)

# esep 4

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)