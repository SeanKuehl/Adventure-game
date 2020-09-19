#make a function that ends the game so I dont have to awkwardly do pygame and sys .exit()
#you can turn a maximum of three (3) times before you break the game and two in one direction
#add custom vic/def message to events/items


import pygame
pygame.init()
pygame.event.get()
import sys
from pygame.locals import *
from background import caveSelection, start, startUp
pygame.event.get()
currentCaveSpot = []
screenWidth = 800
screenHeight = 400
picPosW = screenWidth / 2
picPosH = screenHeight / 2
pygame.event.get()
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Adventure")
pygame.event.get()
#myImage = pygame.image.load('background.bmp')
#myImageRect = myImage.get_rect()
#displaySurface.fill((0, 0, 0))
#displaySurface.blit(myImage, (picPosW - myImageRect.center[0], picPosH - myImageRect.center[1]))
pygame.event.get()
#pygame.display.update()

#pictures will be 800 wide by 400 tall
pygame.event.wait()
open = True
pygame.event.get()
def eventHandler():
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#Django is installed, how to use it I will need tutorials for
pygame.event.get()

while open == True:
    pygame.event.get()
    eventHandler()
    pygame.event.get()
    #displaySurface.blit(myImage, (picPosW - myImageRect.center[0], picPosH - myImageRect.center[1]))
    #pygame.display.update()
    pygame.event.get()
    #displaySurface.fill((0, 0, 0))
    if startUp == True:
        pygame.event.wait()
        start(caveSelection, startUp, 0, currentCaveSpot)













