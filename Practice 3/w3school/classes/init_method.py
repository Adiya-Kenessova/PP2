#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

#ex
#Note: The __init__() method is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name) #Emil
print(p1.age) #36



#Create a class without __init__():
class Person:
  pass
  
p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


#Set a default value for the age parameter:
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
    
p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age) #Emil 18
print(p2.name, p2.age) #Tobias 25


