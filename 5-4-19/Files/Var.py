import pygame, sys, time, os
from pygame.locals import *
pygame.init()

# This is where the keyboard inputs are stored
# Here, just use keyDOWN, keyUP, keyLEFT, and keyRIGHT without the Var.
# in other documents, import Var from Files and use Var.keyDOWN, etc.

# These variables register as TRUE when held down
keyUP = False
keyDOWN = False
keyLEFT = False
keyRIGHT = False

keyLSHIFT = False

# These variables only register as TRUE once, when pressed (NOT when held down)
keySPACE = False
mouseCLICK = False
mouseDOWNPOS = (0, 0)
mouseDOWN = False

keyENTER = False

# This return the tuple (x, y) of mouse positions. Possibly use in conjuction with mouseCLICK == True for collisions with sprites
# You can also replace the position in self.movetto() with mousePOS to make a Sprite follow your mouse
mousePOS = (0, 0)

# Calculus
Answer = None

Ammo = 8
# Number of Zombies on screen at a time. Change it as totalKilled changes
screenZombies = 5
totalKilled = 0
