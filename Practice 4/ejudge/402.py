n = int(input())
gen = (x for x in range(0, n + 1, 2))

first = True
for num in gen:
    if not first:
        print(",", end="")
    print(num, end="")
    first = False


'''n =  int(input())
list1 = (str(x) for x in range(0,n+1) if x%2==0)
#() takes nums when needed, without storing alot of nums in storage, 
#describes the path
print(",".join(list1))'''