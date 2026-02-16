#arg name: fname
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


'''From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.'''

#ex
def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument

#This function expects 2 arguments, and gets 2 arguments::
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
#Error:
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil") #1 arg


#Default parameter
def my_function(name = "friend"):
  print("Hello", name)
my_function("Emil") #Hello, Emil
my_function("Tobias")
my_function() #Hello, friend
my_function("Linus")

#You can send arguments with the key = value syntax.
#The phrase Keyword Arguments is often shortened to kwargs in Python documentation.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog") #order doesnt matter now

#You can mix positional and keyword arguments in a function call.
#However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("dog", name = "Buddy", age = 5)


#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments. To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)
my_function("Emil")

#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")

#You can combine both argument types in the same function.
#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)
