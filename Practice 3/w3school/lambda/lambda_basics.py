#A lambda function is a small anonymous function that can have only one expression
#lambda arguments : expression

#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b 
print(x(5, 6)) #30


#myfunc(n) returns a new function that multiplies its input by n.
'''mydoubler = myfunc(2) creates a function that multiplies by 2.
The returned lambda remembers n (this is called a closure).
So mydoubler(11) → 11 * 2 → 22.'''

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) 
print(mydoubler(11))

#n → fixed earlier (when making the function)
#a → given later (when using the function)
