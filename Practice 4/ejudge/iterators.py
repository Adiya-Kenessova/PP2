#An iterator is an object that contains a countable number of values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#Lists, tuples, dictionaries, and sets are all iterable objects(containers)
#ex
mytuple = ("apple", "banana", "cherry") #tuple
myit = iter(mytuple)

print(next(myit))      #apple
print(next(myit))      #banana
print(next(myit))      #cherry

#We can also use a for loop to iterate through an iterable object.
#The for loop actually creates an iterator object and executes the next() method for each loop.

'''The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.'''
#ex
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))    #1
print(next(myiter))    #2
print(next(myiter))    #3
print(next(myiter))    #4 
print(next(myiter))    #5

#In the __next__() method,we can add a terminating condition to raise an error if the iteration is done a specified number of times (StopIteration)
#ex
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)                   #will print until 20 and stop

