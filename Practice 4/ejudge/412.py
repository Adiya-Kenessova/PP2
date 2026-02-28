from json import loads, dumps

a = input()
b = input()

x = loads(a)
y = loads(b)

def diff(a,b, path=""):
    key = (set(a.keys()) | set(b.keys()))
    diffs = []

    for k in key:
        new_path = f"{path}.{k}" if path else k

        v1 = a.get(k, "<missing>") #the value for key if it exists, otherwise it returns default.
        v2 = b.get(k, "<missing>")

        if isinstance(v1, dict) and isinstance(v2, dict):
            diffs.extend(diff(v1, v2, new_path))

        elif v1 != v2:
            diffs.append(f"{new_path} : {dumps(v1, separators=(',', ':'))} -> {dumps(v2, separators=(',', ':'))}")

    return diffs

res = diff(x,y)

if res:
    for line in sorted(res):
        print(line)
else:
    print("No differences")
    
