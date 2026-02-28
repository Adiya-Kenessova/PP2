def prime(n):
    for i in range(2, n+1):
        check = True
        for g in range(2, i):
            if i%g==0 and i!=g:
                check = False
                break
        if check:
            yield i

n = int(input())

first = True
for num in prime(n):
    if not first:
        print(" ", end="")
    print(num, end="")
    first = False
