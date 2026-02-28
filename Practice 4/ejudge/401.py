n =  int(input())
list = [x**2 for x in range(1,n+1)]
print(*list, sep="\n")