import re

line = input()
x = re.findall("[A-Z]", line)
print(len(x))