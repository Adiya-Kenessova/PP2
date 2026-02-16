#*args and **kwargs allow functions to accept a unknown number of arguments.

''If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:
Using *args to accept any number of arguments:'''

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#ex
def my_function(*args):
  print("Type:", type(args))                          Type: <class 'tuple'>
  print("First argument:", args[0])                   First argument: Emil
  print("Second argument:", args[1])                  Second argument: Tobias
  print("All arguments:", args)                       All arguments: ('Emil', 'Tobias', 'Linus')
my_function("Emil", "Tobias", "Linus")


#You can combine regular parameters with *args. Regular parameters must come before *args:
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")


#Used when you don’t know how many named arguments will be passed,
#add two asterisks ** before the parameter name. This way, the function will receive a dictionary of arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")


#ex
def my_function(**myvar):
  print("Type:", type(myvar))                                    Type: <class 'dict'>
  print("Name:", myvar["name"])                                  Name: Tobias
  print("Age:", myvar["age"])                                    Age: 30
  print("All data:", myvar)                                      All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}
my_function(name = "Tobias", age = 30, city = "Bergen")

#You can combine regular parameters with **kwargs. Regular parameters must come before **kwargs:
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


#You can use both *args and **kwargs in the same function.
#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

#If you have values stored in a list, you can use * to unpack them into individual arguments:
def my_function(a, b, c):
  return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) #6

#Unpacking Dictionaries with **
def my_function(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

#Remember: Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.
