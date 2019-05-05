import pygame, sys, time, os, random
from pygame.locals import *
from Files import Var, Sprite, InputText, Calculus, Images
pygame.init()

# Setup all sprites and textinput here
WHITE = (255, 255, 255)
Input =  InputText.TextInput(
            initial_string="",
            font_family="Calibri",
            font_size= 30,
            antialias = True,
            text_color= WHITE,
            cursor_color= WHITE,
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35)

text_box = pygame.image.load('Text Box.png')
text_box = pygame.transform.scale(text_box, (Sprite.DISPLAY_X-10, int(Sprite.DISPLAY_Y/6)))

def show_ammo(text):
    # small_font = pygame.font.Font("PixelFont.ttf", 35)
    #text_surface = small_font.render(text, False, (255, 255, 255))
    font = pygame.font.SysFont("calibri", 30)
    textsurface = font.render(str(text), False, WHITE)
    Sprite.DISPLAY.blit(textsurface, (700, 50))
    
def update_input():
    Sprite.DISPLAY.blit(text_box, (0, int(4*Sprite.DISPLAY_Y/5)))
    events = pygame.event.get()        
    Input.update(events)
    Sprite.DISPLAY.blit(Input.get_surface(), (80, 680))
    # Text = Input.get_text()
    if Var.keyENTER:
        Var.Answer = Input.get_text()

    text_ammo = "You have " + str(Var.Ammo) + " chickens."
    show_ammo(text_ammo)


#oneZombie = Sprite.Zombie(Images.Zombie_Image, 2, (50, 50), False)
#Sprite.Zombies.add(oneZombie)
'''for zombie in range(5):
    zomx = random.randint(0, Sprite.DISPLAY_X)
    zomy = random.randint(0, Sprite.DISPLAY_Y)
    zombie = Sprite.Zombie(Images.Zombie_Image, 2, (zomx, zomy), False)
    Sprite.Zombies.add(zombie)
    Sprite.spritesList.add(zombie)'''

Chicken = { 'left' : pygame.image.load('Chicken.png'),
            'standingleft' : pygame.image.load('Chicken.png') }
def shoot_zombies():
    update_input()
    Calculus.show_question()
    if Var.mouseDOWN and Var.Ammo != 0:
        Ammo = Sprite.Ammo(Chicken, 2, (Sprite.Player.posx, Sprite.Player.posy), False)
        Sprite.Bullets.add(Ammo)
    for zombie in Sprite.Zombies:
        zombie.moveto(1, 1, [(Sprite.Player.posx, Sprite.Player.posy)], False)
    for zombie in range(Var.screenZombies - (len(Sprite.Zombies))):
        zomx = random.randint(0, Sprite.DISPLAY_X)
        zomy = random.randint(0, Sprite.DISPLAY_Y)
        zombie = Sprite.Zombie(Images.Zombie_Image, 2, (zomx, zomy), False)
        Sprite.Zombies.add(zombie)
        Sprite.spritesList.add(zombie)
