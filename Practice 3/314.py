n = int(input())
arr = list(map(int, input().split()))
q = int(input())

operations = []

for i in range(q):
    op = input().split()
    if op[0] == "add":
        x = int(op[1])
        operations.append(lambda a, x=x: a + x) #x=x in the lambda is needed to “freeze” the value of x inside the lambda.
    elif op[0] == "multiply":
        x = int(op[1])
        operations.append(lambda a, x=x: a * x)
    elif op[0] == "power":
        x = int(op[1])
        operations.append(lambda a, x=x: a ** x)
    elif op[0] == "abs":
        operations.append(lambda a: abs(a))

for i in range(n):
    for f in operations:
        arr[i] = f(arr[i])

print(*arr)
