import math
import os

import pygame

gameStage = 1
startMenuButtons = ["Continue", "New Game", "Settings", "Exit"]

# Initializes PyGame #
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((1088, 768))
pygame.display.set_caption("Menu Testing")
font = pygame.font.SysFont("ariel", 35)
pygame.mouse.set_visible(False)
menuButton = 0
color = (255, 0, 0)

while gameStage == 1:
    for event in pygame.event.get():
        # Close game
        if event.type == pygame.QUIT:
            gameStage = 0
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if menuButton + 1 > len(startMenuButtons) - 1:
                    menuButton = 0
                else:
                    menuButton += 1

            if event.key == pygame.K_w:
                if menuButton - 1 < 0:
                    menuButton = 3
                else:
                    menuButton -= 1
            if event.key == pygame.K_RETURN:
                if menuButton == 0:
                    print("Continue Coming Soon...")
                elif menuButton == 1:
                    gameStage = 2
                elif menuButton == 2:
                    print("Settings Coming Soon...")
                elif menuButton == 3:
                    gameStage = 0
                    running = False

    menuY = math.ceil(384 / (len(startMenuButtons) / 2))
    for button in startMenuButtons:
        if button == startMenuButtons[menuButton]:
            color = (255, 255, 255)
        else:
            color = (255, 0, 0)
        text = font.render(button, True, color)
        screen.blit(text,
                    (544 - text.get_width() // 2, (menuY - text.get_height() // 2)))
        menuY += 64
    pygame.display.update()
