n = int(input())
nums = list(map(int, input().split()))[:n]
nums.sort()
print(*nums[::-1])