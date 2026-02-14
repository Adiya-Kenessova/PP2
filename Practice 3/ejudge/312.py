class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def total_salary(self):
        return self.base_salary
    
class Manager(Employee):
    def __init__(self, name, base_salary, bouns_percent):
        self.bouns_percent = bouns_percent
        super().__init__(name, base_salary)

    def total_salary(self):        
        return self.base_salary * (1 + self.bouns_percent/100)
    
class Developer(Employee):
    def __init__(self, name, base_salary,completed_projects):
        self.completed_projects = completed_projects
        super().__init__(name, base_salary)
        
    def total_salary(self):    
        return self.base_salary + self.completed_projects * 500
    
class Intern(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def total_salary(self):
        return self.base_salary
    
line  = input().split()
role = line[0]
name = line[1]
base_salary = int(line[2])


if role == "Manager":
    bonus_percent = int(line[3])
    employee = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    completed_projects = int(line[3])
    employee = Developer(name, base_salary, completed_projects)
elif role == "Intern":
    employee = Intern(name, base_salary)

print(f"Name: {employee.name}, Total: {employee.total_salary():.2f}")

    
