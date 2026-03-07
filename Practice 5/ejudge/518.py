from re import escape, findall

S = input()
P = input()
x = escape(P)
y = findall(x, S)
print(len(y))