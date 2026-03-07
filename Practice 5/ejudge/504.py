import re

line = input()
x = re.findall(r"\d", line)
if len(x) > 0:
    print(*x, sep=" ")