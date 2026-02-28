#ex1
import math

deg = float(input())
rad = deg * math.pi / 180
print("raian:", round(rad, 6))

#ex2
import math

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

area = (a+b) * h/2
print("Expected Output:", area)

#ex3
import math

n = int(input())
s = float(input())

area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 6))

#ex4
import math

b = float(input())
h = float(input())

area = b*h
print(area)
