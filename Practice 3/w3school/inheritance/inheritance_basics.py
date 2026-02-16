#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class Student(Person):
  pass
#ex
class Person: #parent
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): #child class
  pass

x = Student("Mike", "Olsen")
x.printname() #Mike Olsen



#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # call parent constructor
        self.grade = grade            # new instance variable


