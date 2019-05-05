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
    
    Sprite.DISPLAY.fill((100,120,80))
    Sprite.Bullets.update()
    Sprite.Player.update()
    Sprite.Zombies.update()

    Sprite.drawSprites(Sprite.spritesList)

    Thing.shoot_zombies()
    
    pygame.display.update()
    fpsClock.tick(FPS)
