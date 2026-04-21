import pygame

scr = pygame.display.set_mode((400,400))

class MusicPlayer:
    def __init__(self):
        self.playlist = [
            "music/Swim-Chase Atlantic.mp3",
            "music/Into it-Chase Atlantic.mp3",
            "music/Friends-Chase Atlantic.mp3"
        ]
        self.cover = [
            "music/Swim.jpg",
            "music/Into it.jpg",
            "music/Friends.jpg"
        ]
        self.index = 0
        self.is_playing = False
    

    def play(self):
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        self.is_playing = True
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False


    def next(self):
        self.index += 1
        if self.index >= len(self.playlist):
            self.index = 0
        self.play()
    def previous(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.playlist) - 1
        self.play()

    def get_cover(self):
        return self.cover[self.index]