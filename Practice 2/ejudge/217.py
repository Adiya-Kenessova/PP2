n =int(input())
nums = []
for i in range(n):
    nums.append(input())

cnt_3 = 0
for i in nums:
    cnt = 0
    for x in nums:
        if x == i:
            cnt+=1
    if cnt == 3:
        cnt_3+=1
        nums = [x for x in nums if x !=i]

print(cnt_3)
