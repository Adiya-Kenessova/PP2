def squares(a,b):
    for i in range(a, b+1):
        yield i**2

a,b = map(int, input().split())

first = True
for num in squares(a,b):
    if not first:
        print("", end="")
    print(num, end="\n")
    first = False