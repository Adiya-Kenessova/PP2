from re import search

s = input()
subs = input()
x = search(subs, s)
if x:
    print("Yes")
else:
    print("No")
