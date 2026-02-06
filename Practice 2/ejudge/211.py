n,l,r = map(int, input().split())
nums = list(map(int, input().split()))[:n]
start = l-1
nums[start:r] = reversed(nums[start:r])
print(*nums)

#2
"""left = l - 1
right = r - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left] # Меняем местами
    left += 1
    right -= 1"""