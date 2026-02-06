n = int(input())
lists = {}

for i in range(n):
    line = input().split()
    cmnd = line[0]

    if cmnd == "set":
        key, value = line[1], line[2]
        lists[key] = value

    if cmnd == "get":
        key = line[1]
        if key in lists:
            print(lists[key])
        else:
            print(f"KE: no key {key} found in the document")
