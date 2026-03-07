from re import search

l = input()
x = search(r"Name:\s(.+?),\sAge:\s(.+)", l) #(.+?)  group 1, (.+) group 2
print(x.group(1), x.group(2))