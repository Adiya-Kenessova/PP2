n = int(input())
nums = list(map(int, input().split()))[:n]
max_val = max(nums)
min_val = min(nums)
new = nums.copy()
for i in range(n):
    if new[i] == max_val:
        new[i] = min_val
print(*new)