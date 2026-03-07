from re import findall

s = input()
subs = input()
x = findall(subs, s)
print(len(x))
