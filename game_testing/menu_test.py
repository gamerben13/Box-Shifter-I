import os

import pygame

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((1088, 768))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
