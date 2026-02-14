class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
    
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

name, gpa = input().split()
gpa = float(gpa)

p1 = Person(name)
p2 = Student(name, gpa)

p2.display()
