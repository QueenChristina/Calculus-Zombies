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

def event_loop():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Var.mouseDOWNPOS = Var.mousePOS
            Var.mouseDOWN = True
        else:
            Var.mouseDOWN = False
RUNNING = True
while RUNNING == True:
    variables()
    Var.mousePOS = pygame.mouse.get_pos()

    Sprite.DISPLAY.fill((60,70,80))
        
    if Var.in_class == True:
        Thing.shoot_zombies()

    elif Var.you_died == True:
        Thing.you_died()

        event_loop()
        
    elif Var.calculator == True:
        Thing.calculator()

        event_loop()
        
    elif Var.menu == True:
        Thing.do_menu()
        #BEWARE! Pygame will "not respond" and crash if no event loop is taking place (assumption by OS). Use below if you want no event to be registered
        # pygame.event.pump()
        # NOTE: Your event loop is currently in INPUTTEXT. IF not using INPUTTEXT, use the below event loop so can close program
        event_loop() 
    else:
        pygame.event.pump()
    
    pygame.display.update()
    fpsClock.tick(FPS)
