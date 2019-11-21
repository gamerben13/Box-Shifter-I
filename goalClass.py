import pygame


class goal(object):
    def __init__(self, startX, startY):
        self.image = pygame.image.load("game_art/goal.png")
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY

    def boxInGoal(self, boxes):
        for box in boxes:
            if box.hitBox.colliderect(self.hitBox):
                return True

    def draw(self, surface):
        surface.blit(self.image, self.hitBox)
