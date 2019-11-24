# Import Library's
import math
import os

import pygame

import boxClass
import goalClass
import holeClass
import playerClass
import wallClass

# Initialize Variables #
running = True
debug = False
player = None
block = None
walls = []
goals = []
holes = []
boxes = []
objects = []
startMenuButtons = ["Continue", "New Game", "Settings", "Quit"]
gameStage = 1
level = 0
mouseState = 0

# Levels #
levels = [
    [
        'WWWWWWWWWWWWWWWWW',
        'WWW           WWW',
        'WW             WW',
        'W               W',
        'W               W',
        'W  P    B    G  W',
        'W               W',
        'W               W',
        'W               W',
        'WW             WW',
        'WWW           WWW',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'W    W    B   GGW',
        'W P  W          W',
        'W    WWWWW   WWWW',
        'W       WW      W',
        'W       WWWW    W',
        'W          W    W',
        'WWWWWW          W',
        'W    W          W',
        'W B      W      W',
        'W        W      W',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'WWWW  WWW      WW',
        'WW    WWW  B   WW',
        'W     WWW    W GW',
        'W P    W        W',
        'W       B WW W  W',
        'W     B      WWWW',
        'W      W     WWWW',
        'W     WWWW WWWWWW',
        'W     WWWWGWWWWWW',
        'W  G  WWWWWWWWWWW',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'W      WWW      W',
        'W               W',
        'W       P       W',
        'W    W GWG W    W',
        'WW WWWWWWWWWWW WW',
        'W   W  GWG  W   W',
        'W               W',
        'W      WWW      W',
        'W   B B W B B   W',
        'W       W       W',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'W     GW        W',
        'WWW  WWW P      W',
        'W      WWWWW    W',
        'W      W   WW  WW',
        'W      G   W    W',
        'W      W   WB   W',
        'WWWBWWWW        W',
        'W      B        W',
        'W      WW  W  B W',
        'WWWWWWWWG  W    W',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'W   WWWWWWWWW   W',
        'W      WWW  B   W',
        'W       W       W',
        'W       W       W',
        'W G     H B   P W',
        'W G     H B     W',
        'W       W       W',
        'W       W       W',
        'W      WWW  B   W',
        'W   WWWWWWWWW   W',
        'WWWWWWWWWWWWWWWWW',
    ],
    [
        'WWWWWWWWWWWWWWWWW',
        'W          G B  W',
        'W          WWW WW',
        'W  WWW   W     WW',
        'W  W     W     WW',
        'W BW     W  W WWW',
        'W  W  W  W  W WWW',
        'WWWW  W  WWWWHWWW',
        'W     W   W  P  W',
        'W GG    B W B   W',
        'W     W   W     W',
        'WWWWWWWWWWWWWWWWW',
    ]
]

# Initializes PyGame #
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((1088, 768))
pygame.display.set_caption("Box Shifter I")
pygame.display.set_icon(pygame.image.load("game_art/icon.png"))
font = pygame.font.SysFont("ariel", 35)
pygame.mouse.set_visible(False)
menuButton = 0
color = (255, 0, 0)

while running:
    if gameStage == 1:
        walls = []
        boxes = []
        goals = []
        holes = []
        objects = []
        player = None
        debug = False
    while gameStage == 1:
        screen.fill((0, 0, 0))
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

    if gameStage == 2:
        walls = []
        boxes = []
        goals = []
        holes = []
        objects = []
        player = None
        debug = False
        levelX = levelY = 0
        for row in levels[level]:
            for col in row:
                if col == "W":
                    walls.append(wallClass.wall(levelX, levelY))
                if col == "B":
                    boxes.append(boxClass.box(levelX, levelY))
                if col == "P":
                    player = playerClass.player(levelX, levelY)
                if col == "G":
                    goals.append(goalClass.goal(levelX, levelY))
                if col == "H":
                    holes.append(holeClass.hole(levelX, levelY))
                levelX += 64
            levelY += 64
            levelX = 0
        objects.append(walls)
        objects.append(holes)
    while gameStage == 2:
        score = 0
        screen.fill((200, 200, 200))
        # Get events
        # Draw debug grid
        if debug:
            for i in range(0, int(1088 / 64)):
                pygame.draw.line(screen, (0, 0, 0), (i * 64, 0), (i * 64, 768))

            for i in range(0, int(768 / 64)):
                pygame.draw.line(screen, (0, 0, 0), (0, i * 64), (1088, i * 64))

        for event in pygame.event.get():
            # Close game
            if event.type == pygame.QUIT:
                gameStage = 0
                running = False

            # Key Pressed
            if event.type == pygame.KEYDOWN:
                # F3 to enable and disable debug
                if event.key == pygame.K_F3:
                    if debug:
                        debug = False
                    else:
                        debug = True
                if event.key == pygame.K_r:
                    walls = []
                    boxes = []
                    goals = []
                    holes = []
                    objects = []
                    levelX = levelY = 0
                    for row in levels[level]:
                        for col in row:
                            if col == "W":
                                walls.append(wallClass.wall(levelX, levelY))
                            if col == "B":
                                boxes.append(boxClass.box(levelX, levelY))
                            if col == "P":
                                player = playerClass.player(levelX, levelY)
                            if col == "G":
                                goals.append(goalClass.goal(levelX, levelY))
                            if col == "H":
                                holes.append(holeClass.hole(levelX, levelY))
                            levelX += 64
                        levelY += 64
                        levelX = 0
                    objects.append(walls)
                    objects.append(holes)

                if event.key == pygame.K_SLASH:
                    gameStage = 3

                player.move(pygame.key.get_pressed(), objects, boxes)

        for wall in walls:
            wall.draw(screen)
        for hole in holes:
            hole.draw(screen)
        for goal in goals:
            if goal.boxInGoal(boxes):
                score += 1
            goal.draw(screen)
        for box in boxes:
            box.draw(screen)

        if score == len(goals):
            if len(levels) <= level + 1:
                gameStage = 1
                walls = []
            else:
                level += 1
                break

        player.draw(screen)
        pygame.display.update()

    if gameStage == 3:
        mouseState = 1
        walls = []
        boxes = []
        goals = []
        holes = []
        player = None
        debug = True
        block = None
        levelX = levelY = 0
        customLevel = [
            "WWWWWWWWWWWWWWWWW",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "W               W",
            "WWWWWWWWWWWWWWWWW"
        ]
        for row in customLevel:
            for col in row:
                if col == "W":
                    walls.append(wallClass.wall(levelX, levelY))
                if col == "B":
                    boxes.append(boxClass.box(levelX, levelY))
                if col == "P":
                    player = playerClass.player(levelX, levelY)
                if col == "G":
                    goals.append(goalClass.goal(levelX, levelY))
                if col == "H":
                    holes.append(holeClass.hole(levelX, levelY))
                levelX += 64
            levelY += 64
            levelX = 0
        objects.append(walls)
        objects.append(holes)
    while gameStage == 3:
        mousePos = pygame.mouse.get_pos()
        screen.fill((100, 100, 100))
        # Draw debug grid
        if debug:
            for i in range(0, int(1088 / 64)):
                pygame.draw.line(screen, (0, 0, 0), (i * 64, 0), (i * 64, 768))

            for i in range(0, int(768 / 64)):
                pygame.draw.line(screen, (0, 0, 0), (0, i * 64), (1088, i * 64))

        for event in pygame.event.get():
            # Close game
            if event.type == pygame.QUIT:
                gameStage = 0
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SLASH:
                    gameStage = 2
                if event.key == pygame.K_p:
                    customLevel = [
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 ",
                        "                 "
                    ]
                    levelX = levelY = 0
                    fRow = ""
                    i = 0
                    for row in customLevel:

                        for col in row:
                            for wall in walls:
                                if wall.hitBox.x == levelX and wall.hitBox.y == levelY:
                                    col = "W"
                            for goal in goals:
                                if goal.hitBox.x == levelX and goal.hitBox.y == levelY:
                                    col = "G"
                            for box in boxes:
                                if box.hitBox.x == levelX and box.hitBox.y == levelY:
                                    col = "B"
                            for hole in holes:
                                if hole.hitBox.x == levelX and hole.hitBox.y == levelY:
                                    col = "H"
                            if player is not None:
                                if player.hitBox.x == levelX and player.hitBox.y == levelY:
                                    col = "P"
                            fRow += col
                            levelX += 64

                        levelY += 64
                        levelX = 0
                        customLevel[i] = fRow
                        fRow = ""
                        i += 1
                    print("####### NEW CUSTOM LEVEL #######")
                    print(",\n[")
                    i = 0
                    for row in customLevel:
                        if i == len(customLevel):
                            print(repr(row))
                        else:
                            print(repr(row) + ",")
                        i += 1
                    print("]")

                if event.key == pygame.K_F3:
                    if debug:
                        debug = False
                    else:
                        debug = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:
                    if mouseState - 1 > 6 or mouseState - 1 < 1:
                        mouseState = 6
                    else:
                        mouseState -= 1
                if event.button == 5:
                    if mouseState + 1 > 6 or mouseState + 1 < 1:
                        mouseState = 1
                    else:
                        mouseState += 1
                if event.button == 1:
                    if mouseState == 1:
                        walls.append(wallClass.wall((math.ceil(mousePos[0] / 64) - 1) * 64,
                                                    (math.ceil(mousePos[1] / 64) - 1) * 64))
                    if mouseState == 2:
                        boxes.append(boxClass.box((math.ceil(mousePos[0] / 64) - 1) * 64,
                                                  (math.ceil(mousePos[1] / 64) - 1) * 64))
                    if mouseState == 3:
                        goals.append(goalClass.goal((math.ceil(mousePos[0] / 64) - 1) * 64,
                                                    (math.ceil(mousePos[1] / 64) - 1) * 64))
                    if mouseState == 4:
                        player = playerClass.player((math.ceil(mousePos[0] / 64) - 1) * 64,
                                                    (math.ceil(mousePos[1] / 64) - 1) * 64)
                    if mouseState == 5:
                        holes.append(holeClass.hole((math.ceil(mousePos[0] / 64) - 1) * 64,
                                                    (math.ceil(mousePos[1] / 64) - 1) * 64))
                    if mouseState == 6:
                        for wall in walls:
                            if wall.hitBox.y == (math.ceil(mousePos[1] / 64) - 1) * 64 and wall.hitBox.x == (
                                    math.ceil(mousePos[0] / 64) - 1) * 64:
                                walls.remove(wall)
                        for goal in goals:
                            if goal.hitBox.y == (math.ceil(mousePos[1] / 64) - 1) * 64 and goal.hitBox.x == (
                                    math.ceil(mousePos[0] / 64) - 1) * 64:
                                goals.remove(goal)
                        for box in boxes:
                            if box.hitBox.y == (math.ceil(mousePos[1] / 64) - 1) * 64 and box.hitBox.x == (
                                    math.ceil(mousePos[0] / 64) - 1) * 64:
                                boxes.remove(box)
                        if player is not None:
                            if player.hitBox.y == (math.ceil(mousePos[1] / 64) - 1) * 64 and player.hitBox.x == (
                                    math.ceil(mousePos[0] / 64) - 1) * 64:
                                player = None
        if mouseState == 1:
            block = wallClass.wall((math.ceil(mousePos[0] / 64) - 1) * 64, (math.ceil(mousePos[1] / 64) - 1) * 64)
        elif mouseState == 2:
            block = boxClass.box((math.ceil(mousePos[0] / 64) - 1) * 64, (math.ceil(mousePos[1] / 64) - 1) * 64)
        elif mouseState == 3:
            block = goalClass.goal((math.ceil(mousePos[0] / 64) - 1) * 64, (math.ceil(mousePos[1] / 64) - 1) * 64)
        elif mouseState == 4:
            block = playerClass.player((math.ceil(mousePos[0] / 64) - 1) * 64, (math.ceil(mousePos[1] / 64) - 1) * 64)
        elif mouseState == 5:
            block = holeClass.hole((math.ceil(mousePos[0] / 64) - 1) * 64, (math.ceil(mousePos[1] / 64) - 1) * 64)
        pygame.mouse.set_visible(True)
        for wall in walls:
            wall.draw(screen)
        score = 0
        for goal in goals:
            goal.draw(screen)
        for box in boxes:
            box.draw(screen)
        for hole in holes:
            hole.draw(screen)
        if player is not None:
            player.draw(screen)
        if mouseState != 6:
            if block is not None:
                block.draw(screen)
        pygame.display.update()
