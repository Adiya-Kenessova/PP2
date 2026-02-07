#Examples of comparison operators (==, !=, >, <, >=, <=) that return True/False.
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(not(x > 5))         # False
print(not(x < 5))         # True

#it checks whether a value is considered empty/zero or not.
print(bool("Hello")) #true
print(bool(15)) #true
bool("")        # False (empty string)
bool(0)         # False (zero)
bool(None)      # False
bool([])        # False (empty list)
bool({})        # False (empty dict)

#returns bool by lokking at size, if sixe -> 0, returns 0
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#isinstance(value, type) checks whether a variable belongs to a certain type (class).
x = 200
print(isinstance(x, int))    #True
print(isinstance(x, int))     # True
print(isinstance(x, float))   # False
print(isinstance(x, str))     # False
