import re

l = input()
a = re.compile(r"\b\w+\b")
x = re.findall(a, l)
print(len(x))
