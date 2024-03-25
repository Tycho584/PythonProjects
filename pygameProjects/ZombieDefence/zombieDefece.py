import pygame, random, time, math, keyboard, os
import playerLibrary

pygame.init()

screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()

player = playerLibrary.Player(screen, 1000, 400)
player.initialLoadOfPlayer()

screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break

    player.checkIfPlayerShouldBeMoved()
    player.loadPlayeronScreen(screen)
    pygame.display.flip()