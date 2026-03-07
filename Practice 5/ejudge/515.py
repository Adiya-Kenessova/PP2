from re import sub

l = input()
x = sub(r"\d", lambda m: m.group() * 2, l)
print(x)

#group() returns only the characters that regex pattern grabs