n = int(input())
nums = list(map(int, input().split()))[:n]
newbie = set()
for i in nums:
    if(i not in newbie):
        newbie.add(i)
        print("YES")
    else:
        print("NO")
