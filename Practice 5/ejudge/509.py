import re

line = input()
x = re.findall(r"\b\w{3}\b", line)
print(len(x))