def if_valid(a):
    b = a
    cnt = 0
    total = 0
    while b > 0:
        if (b % 10) % 2 == 0:
            cnt+=1
        b//=10
        total+=1
    if cnt == total:
        print("Valid") 
    else:
        print("Not valid")

n = int(input())
if_valid(n)

