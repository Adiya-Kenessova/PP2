#Creating multiple methods with the same name but different parameters.
def add(a, b):
    return a+b

def add(a, b, c):
    return a+b+c
print(add(2,3))  # ❌ Error! Only 3-arg version exists


#use instead:
def add(a, b, c=0):
    return a + b + c
print(add(2,3))    # 5 → uses default c=0
print(add(2,3,4))  # 9 → uses provided c


def add(*args):
    return sum(args)
print(add(2,3))       # 5
print(add(2,3,4,5))   # 14

