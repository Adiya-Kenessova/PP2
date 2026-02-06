n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in nums:
    if(i > 0):
        cnt+=1
    else:
        continue
print(cnt) 