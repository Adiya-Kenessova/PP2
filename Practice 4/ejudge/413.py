from json import loads, dumps

j = loads(input())
q = int(input())

def getval(j, qry):
    curr = j
    for part in qry.split('.'):
        while '[' in part:

            idx1 = part.index('[')
            key = part[:idx1]
            if key:
                if not isinstance(curr, dict) or key not in curr:
                    return "NOT_FOUND"
                curr = curr[key]

            while '[' in part:
                idx1 = part.index('[')
                idx2 = part.index(']')
                i = int(part[idx1+1:idx2])
                if not isinstance(curr, list) or i >= len(curr):
                    return "NOT_FOUND"
                curr = curr[i]
                part = part[idx2+1:]

        if part:
            if not isinstance(curr, dict) or part not in curr:
                return "NOT_FOUND"
            curr = curr[part]
    return dumps(curr, separators=(",", ":"))

for _ in range(q):
    print(getval(j, input()))