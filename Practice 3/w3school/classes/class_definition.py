#A Class is like an object constructor, or a "blueprint" for creating objects.
#To create a class, use the keyword class:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) #5

#You can delete objects by using the del keyword:
del p1


#You can create multiple objects from the same class. Note: Each object is independent and has its own copy of the class properties.

class Person:
  pass
