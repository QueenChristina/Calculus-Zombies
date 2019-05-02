import pygame, sys, time, os
from pygame.locals import *
from Files import Var, Sprite, InputText
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


def update_input():
    Sprite.DISPLAY.blit(text_box, (0, int(4*Sprite.DISPLAY_Y/5)))
    events = pygame.event.get()        
    Input.update(events)
    Sprite.DISPLAY.blit(Input.get_surface(), (80, 680))
    # Text = Input.get_text()
    if Var.keyENTER:
        Var.Answer = Input.get_text()

