def fibonacci(n):
    if n == 0:
        return
    elif n == 1:
        yield 0
    a, b = 0, 1
    for i in range(n-1):
        if i==0:
            yield 0
        if i==1:
            yield 1
        else:
            a, b= b, a+b
            yield b

n = int(input())

first = True
for num in fibonacci(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False
