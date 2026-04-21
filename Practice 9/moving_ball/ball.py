import pygame

class Ball():
    def __init__(self, cent_x, cent_y, width, height):
        self.width = width
        self.height = height
        self.x = cent_x
        self.y = cent_y
        self.rad = 25
        self.speed = 20

    def move_up(self):
        if self.y - self.speed - self.rad >=0:
            self.y -= self.speed
    def move_down(self):
        if self.y + self.speed + self.rad <= self.height:
            self.y += self.speed
    def move_right(self):
        if self.x + self.speed + self.rad <= self.width:
            self.x += self.speed
    def move_left(self):
        if self.x - self.speed - self.rad >=0:
            self.x -= self.speed

    

            