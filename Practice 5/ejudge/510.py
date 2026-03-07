import re

line = input()
x = re.findall("cat|dog", line)
if x:
    print("Yes")
else:
    print("No")