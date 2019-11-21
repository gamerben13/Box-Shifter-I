import pygame


class box(object):
    def __init__(self, startX, startY):
        self.image = pygame.image.load("game_art/box.png")
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY

    def draw(self, surface):
        surface.blit(self.image, self.hitBox)
