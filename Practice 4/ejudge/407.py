class Reverse:
    def __init__(self):
        self.s = input()
    def get(self):
        print(*reversed(self.s), sep="")

S = Reverse()
S.get()