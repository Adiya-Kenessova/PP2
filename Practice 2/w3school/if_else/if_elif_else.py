# 1. An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")


#2. If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

#3. The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")


#4. The else statement is executed when the if condition (and any elif conditions) evaluate to False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
