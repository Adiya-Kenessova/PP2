import re

line = input()
pttrn = r"\S+@\S+\.\S+"
x = re.search(pttrn, line)
if x:
    print(x.group())
else:
    print("No email")



