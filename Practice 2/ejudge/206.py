n = int(input())
nums = list(map(int, input().split()))
print(max(nums))

#2 
max1 = 0
for i in nums:
    if i>max:
        max = i
    else:
        continue
print(max1)