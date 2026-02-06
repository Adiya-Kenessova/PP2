n = int(input())
nums = list(map(int, input().split()))
max = nums[0]
pos_max = 1
cur = 1
for i in nums:
    if i>max:
        max = i
        pos_max = cur
    cur+=1
print(pos_max)