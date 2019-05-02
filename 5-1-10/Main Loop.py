import pygame, sys, time, os, sympy
from pygame.locals import *
from Files import Sprite, Var, Images, InputText, Thing, Calculus
pygame.init()

FPS=40
fpsClock= pygame.time.Clock()

# LATER, to optimize performance time, use: https://www.pygame.org/docs/tut/newbieguide.html


def variables():
    keys = pygame.key.get_pressed()
    keyLEFT = keys[pygame.K_LEFT]
    keyRIGHT = keys[pygame.K_RIGHT]
    keyDOWN = keys[pygame.K_DOWN]
    keyUP = keys[pygame.K_UP]

    if keyDOWN:
        Var.keyDOWN = True
    elif keyUP:
        Var.keyUP = True
    if keyLEFT:
        Var.keyLEFT = True
    elif keyRIGHT:
        Var.keyRIGHT = True

    if not keyDOWN:
        Var.keyDOWN = False
    if not keyUP:
        Var.keyUP = False
    if not keyLEFT:
        Var.keyLEFT = False
    if not keyRIGHT:
        Var.keyRIGHT = False

    if keys[pygame.K_LSHIFT]:
        Var.keyLSHIFT = True

    if not keys[pygame.K_LSHIFT]:
        Var.keyLSHIFT = False

RUNNING = True
while RUNNING == True:
    variables()
    Var.mousePOS = pygame.mouse.get_pos()
    
    Sprite.DISPLAY.fill((60,70,80))
    Sprite.objList.update()
    Sprite.Player.update()
    
    # Note, please change layers depending on y value: https://www.reddit.com/r/pygame/comments/3de4ng/challenge_drawing_in_the_right_order/
    # Answer: https://github.com/iminurnamez/draw-order-challenge/commit/387da00cf21e63d0cddee61737df3edd91aa59b4
    
    pygame.draw.rect(Sprite.DISPLAY, (200, 10, 15), Sprite.Player.colliderect, 2)



    Sprite.drawSprites(Sprite.spritesList)

    Thing.update_input()
    Calculus.show_question()
    
    pygame.display.update()
    fpsClock.tick(FPS)
