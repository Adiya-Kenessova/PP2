class Pair:
    def __init__(self, a, b):
        self.a =a
        self.b = b
    
    def add(self, a1, b1):
        a_sum = self.a + a1
        b_sum = self.b + b1
        return f"Result: {a_sum} {b_sum}"

a1, b1, a2, b2 = map(int, input().split())
p1 = Pair(a1, b1)
print(p1.add(a2,b2))
