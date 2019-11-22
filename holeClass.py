import pygame


class hole(object):
    def __init__(self, startX, startY):
        self.image = pygame.image.load("game_art/hole.png")
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY

    def draw(self, surface):
        surface.blit(self.image, self.hitBox)

