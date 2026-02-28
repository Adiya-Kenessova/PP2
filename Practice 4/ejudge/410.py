def prr(a,k):
    for i in range(0, k):
        for g in a:
            yield g   

a = list(input().split())
k = int(input())

first = True
for i in prr(a,k):
    if not first:
        print(" ", end="")
    print(i, end="")
    first = False
    
