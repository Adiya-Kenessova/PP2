x = int(input())
check = 0
for i in range(2, x):
    if x % i == 0:
        print("No")
        check = 1
        break
if(check != 1):
    print("Yes")
