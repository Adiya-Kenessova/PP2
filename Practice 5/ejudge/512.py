import re

line = input()
x = re.findall("[0-9]{2,}", line)
print(*x, sep=" ")