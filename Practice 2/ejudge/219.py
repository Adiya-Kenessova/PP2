n =int(input())
doramas = {}
for i in range(n):
    s, k = input().split()
    k = int(k)
    if s in doramas:
        doramas[s] +=k
    else:
        doramas[s] = k

for i in sorted(doramas):
    print(i, doramas[i])




