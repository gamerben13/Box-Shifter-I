import pygame


class player(object):
    def __init__(self, startX, startY):
        self.image = pygame.image.load("game_art/player.png")
        self.hitBox = self.image.get_rect()
        self.hitBox.x = startX
        self.hitBox.y = startY
        self.moves = 0

    def move(self, key, walls, boxes):
        xChange = 0
        yChange = 0
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            xChange = 0
            yChange = 64

        elif key[pygame.K_UP] or key[pygame.K_w]:
            xChange = 0
            yChange = -64

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            xChange = -64
            yChange = 0

        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            xChange = 64
            yChange = 0

        if xChange != 0 or yChange != 0:
            if self.isPushing(boxes, xChange, yChange):
                if self.noWallInBox(boxes, walls, xChange, yChange):
                    playerHitBox = pygame.Rect(self.hitBox[0] + xChange, self.hitBox[1] + yChange, self.hitBox[2],
                                               self.hitBox[3])
                    for box in boxes:
                        if playerHitBox.colliderect(box.hitBox):
                            box.hitBox.x += xChange
                            box.hitBox.y += yChange
                    self.hitBox.x += xChange
                    self.hitBox.y += yChange
                    self.moves += 1

            else:
                if self.canMove(walls, xChange, yChange):
                    self.hitBox.x += xChange
                    self.hitBox.y += yChange
                    self.moves += 1
            return self.moves

    def canMove(self, walls, xChange, yChange):
        playerHitBox = pygame.Rect(self.hitBox[0] + xChange, self.hitBox[1] + yChange, self.hitBox[2], self.hitBox[3])
        for wall in walls:
            if playerHitBox.colliderect(wall.hitBox):
                return False
        return True

    def isPushing(self, boxes, xChange, yChange):
        playerHitBox = pygame.Rect(self.hitBox[0] + xChange, self.hitBox[1] + yChange, self.hitBox[2], self.hitBox[3])
        for box in boxes:
            if playerHitBox.colliderect(box.hitBox):
                return True
        return False

    def noWallInBox(self, boxes, walls, xChange, yChange):
        playerHitBox = pygame.Rect(self.hitBox[0] + xChange, self.hitBox[1] + yChange, self.hitBox[2], self.hitBox[3])
        for box in boxes:
            boxHitBox = pygame.Rect(box.hitBox[0] + xChange, box.hitBox[1] + yChange, box.hitBox[2],
                                    box.hitBox[3])
            if playerHitBox.colliderect(box.hitBox):
                for wall in walls:
                    if boxHitBox.colliderect(wall.hitBox):
                        return False
            for box2 in boxes:
                if boxHitBox.colliderect(box2.hitBox):
                    return False
        return True

    def draw(self, surface):
        surface.blit(self.image, self.hitBox)
