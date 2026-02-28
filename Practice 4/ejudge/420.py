g = 0
n = 0

cnt = int(input())

for i in range(cnt):
    line = input().split()
    scope = line[0]
    val = int(line[1])

    if scope == "global":
        g+=val
    elif scope == "nonlocal":
        n +=val

print(g, n)

