def divisible(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i

n = int(input())

first = True
for num in divisible(n):
    if not first:
        print(" ", end="")
    print(num, end="")
    first = False