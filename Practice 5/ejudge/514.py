import re

line = input()
c = re.compile(r"^\d+$")
x = re.findall(c, line)
if x:
    print("Match")
else:
    print("No match")