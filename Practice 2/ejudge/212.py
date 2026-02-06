n = int(input())
nums = list(map(int, input().split()))[:n]
out = [i**2 for i in nums]
print(*out)