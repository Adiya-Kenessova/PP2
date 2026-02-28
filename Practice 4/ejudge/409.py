def prime(n):
    for i in range(0, n+1):
        yield 2**i

n = int(input())

first = True
for num in prime(n):
    if not first:
        print(" ", end="")
    print(num, end="")
    first = False
