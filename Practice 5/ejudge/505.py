import re

line = input()
x = re.search("^[a-zA-Z].*[0-9]$", line)
if x:
    print("Yes")
else:
    print("No")
