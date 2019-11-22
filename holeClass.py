import pygame


class hole(object):
    def __init__(self, startX, startY):
        self.image = pygame.image.load("game_art/hole.png")
        self.image_fill = pygame.image.load("game_art/holeFill.png")
        self.fill = False
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY

    def draw(self, surface):
        if not self.fill:
            surface.blit(self.image, self.hitBox)
        else:
            surface.blit(self.image_fill, self.hitBox)

