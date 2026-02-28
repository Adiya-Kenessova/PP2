#ex1
def sqr(N):
    for i in range(N+1):
        yield i*i

#ex2
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in even(n)))

#3
def div_by_3_and_4(n):
    for i in range(n+1):
        if i % 12 == 0:
            yield i

n = int(input())
for x in div_by_3_and_4(n):
    print(x, end=" ")
print()

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())
for x in squares(a, b):
    print(x)

#ex5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for x in countdown(n):
    print(x, end=" ")
print()

