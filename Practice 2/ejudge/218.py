n =int(input())
l = []
for i in range(n):
    l.append(input())

out = []
for i in sorted(l):
    if i not in out:
        out.append(i)
        for j in range(n):
            if l[j] == i:
                print(i, j+1)
                break

#ex:
"""5
apple
banana
apple
cherry
banana"""

