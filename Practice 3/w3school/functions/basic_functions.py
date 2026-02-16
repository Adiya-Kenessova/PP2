def my_function():
  print("Hello from a function")

#calling func
def my_function():
print("Hello from a function")
my_function()


#Valid function names:
calculate_sum()
_private_function()
myFunction2()


#With functions, you write the code once and reuse it
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


#Functions can send data back to the code that called them using the return statement.
#When a function reaches a return statement, it stops executing and sends the result back
#If a function doesn't have a return statement, it returns None by default.
def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)
