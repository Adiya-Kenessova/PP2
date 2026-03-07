#1
import re
s = input()
if re.match(r"ab*", s):
    print("Match!")
else:
    print("No match")

#2
import re
s = input()
if re.match(r"ab{2,3}", s):
    print("Match!")
else:
    print("No match")

#3
import re
s = input()
print(re.findall(r"[a-z]+(?:_[a-z]+)+", s))

#4
import re
s = input()
print(re.findall(r"[A-Z][a-z]+", s))

#5
import re
s = input()
if re.search(r"a.*b", s):
    print("Match!")
else:
    print("No match")

#6
import re
s = input()
print(re.sub(r"[ ,\.]", ":", s))

#7
import re
s = input()
camel = re.sub(r"_(\w)", lambda m: m.group(1).upper(), s)
print(camel)

#8
import re
s = input()
print(re.split(r"(?=[A-Z])", s))

#9
import re
s = input()
print(re.sub(r"([A-Z])", r" \1", s).lstrip())

#10
import re
s = input()
print(re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_"))
