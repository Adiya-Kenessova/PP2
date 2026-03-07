import re

line = input()
x = re.findall(r"\w+", line)
print(len(x))