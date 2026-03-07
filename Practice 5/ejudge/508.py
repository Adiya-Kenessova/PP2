from re import split

S = input()
D = input()
x = split(D, S)
print(*x, sep=",")

