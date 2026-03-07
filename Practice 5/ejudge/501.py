from re import match

line = input()
x = match("Hello", line)
if x:
    print("Yes")
else:
    print("No")