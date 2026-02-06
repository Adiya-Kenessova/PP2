n = int(input())
nums = list(map(int, input().split()))[:n]

cnt = []
uniq = []

for i in nums: #4 1 1 3
    if i in uniq:
        cnt[uniq.index(i)] +=1
    else:
        uniq.append(i) 
        cnt.append(1)    

if cnt:
    max1 = max(cnt)

num = []
for i in range(len(uniq)):
    if cnt[i] == max1:
        num.append(uniq[i])

print(min(num))