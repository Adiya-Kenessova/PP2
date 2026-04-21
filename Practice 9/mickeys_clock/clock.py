import datetime
import pygame


class MickeyClock:
    def __init__(self, center):
        self.center = center

    def get_angles(self):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        return sec_angle, min_angle

    def rotate(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect()
        rect.center = self.center
        return rotated, rect