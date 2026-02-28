q = int(input())

for i in range(0,q):
    mod_path, attr = input().split()
    try:
        m = __import__(mod_path)
        for p in mod_path.split('.')[1:]:
            m = getattr(m, p)
    except:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(m, attr):
        print("ATTRIBUTE_NOT_FOUND")
    elif callable(getattr(m, attr)):
        print("CALLABLE")
    else:
        print("VALUE")