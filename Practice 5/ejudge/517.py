from re import findall

l = input()
x = findall(r"\d{2}/\d{2}/\d{4}", l)
print(len(x))