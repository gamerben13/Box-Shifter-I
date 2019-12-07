import pygame
import datetime


class wall(object):
    def __init__(self, startX, startY):
        if int(datetime.date.today().strftime('%m')) == 12:
            if int(datetime.date.today().strftime('%d')) <= 25:
                self.image = pygame.image.load("game_art/wall_christmas.png")
        else:
            self.image = pygame.image.load("game_art/wall.png")
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY

    def draw(self, surface):
        surface.blit(self.image, self.hitBox)
