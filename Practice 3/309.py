import math
pi = 3.14159
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (pi * (r**2))
    
r = int(input())
p1= Circle(r)
print(f"{p1.area():.2f}")
