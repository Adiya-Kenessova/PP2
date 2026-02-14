class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.lenght = length

    def area(self):
        return self.lenght * self.lenght
    
lenght = int(input())
sq = Square(lenght)

print(sq.area())

