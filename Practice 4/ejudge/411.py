from json import loads, dumps

object = input()
patch = input()

o = loads(object)
p = loads(patch)

def check(o, p):
    for k,v in p.items():
        if v is None:
            if k in o:
                del o[k]
        elif k not in o:
            o[k] = v
        elif isinstance(o[k], dict) and isinstance(v, dict):
            check(o[k], v)

        else:
            o[k] = v

    return o

b = check(o, p)
print(dumps(b, sort_keys=True,separators=(",", ":") ))

