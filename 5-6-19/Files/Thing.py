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
text_box_status = pygame.transform.scale(text_box, (220, 90))

def show_text(text, pos):
    # small_font = pygame.font.Font("PixelFont.ttf", 35)
    #text_surface = small_font.render(text, False, (255, 255, 255))
    font = pygame.font.SysFont("calibri", 30)
    textsurface = font.render(str(text), False, WHITE)
    Sprite.DISPLAY.blit(textsurface, pos)
    
def update_input():
    Sprite.DISPLAY.blit(text_box, (0, int(4*Sprite.DISPLAY_Y/5)))
    events = pygame.event.get()        
    Input.update(events)
    Sprite.DISPLAY.blit(Input.get_surface(), (80, 680))
    # Text = Input.get_text()
    if Var.keyENTER:
        Var.Answer = Input.get_text()

    Sprite.DISPLAY.blit(text_box_status, (750,10))
    text_ammo =  str(Var.Ammo) + " chickens"
    text_health = str(Var.Health) + " health"
    show_text(text_ammo,  (780, 30))
    show_text(text_health,  (780, 60))


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
classroom = pygame.image.load(os.path.join('Stuff', 'Classroom.png'))
classroom = pygame.transform.scale(classroom, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))

classroomwall = pygame.image.load(os.path.join('Stuff', 'Classroom Wall.png'))
wall = classroomwall.get_rect()
scaley = Sprite.DISPLAY_X/wall.width
classroomwall = pygame.transform.scale(classroomwall, (Sprite.DISPLAY_X, int(wall.height*scaley)))
classroomwall = pygame.transform.flip(classroomwall, True, False)
ClassWall = Images.autodict(classroomwall,classroomwall, classroomwall, classroomwall,classroomwall,classroomwall)
classroomwall = Sprite.BigObject(ClassWall, 1, (0, 0), False)

Sprite.objList.add(classroomwall)
Sprite.spritesList.add(classroomwall)

time_elapsed = 0
wait_time = 250
def shoot_zombies():
    global time_elapsed, wait_time

    #Sprite.DISPLAY.fill((100,120,80))

    Sprite.DISPLAY.blit(classroom, (0,0))

    Sprite.objList.update()
    
    Sprite.Bullets.update()
    Sprite.Player.update()
    Sprite.Zombies.update()

    

    Sprite.drawSprites(Sprite.spritesList)

    
    update_input()
    Calculus.show_question()
    if Var.mouseDOWN and Var.Ammo != 0:
        Ammo = Sprite.Ammo(Chicken, 2, (Sprite.Player.posx, Sprite.Player.posy), False)
        Sprite.Bullets.add(Ammo)
    for zombie in Sprite.Zombies:
        zombie.moveto(1, 1, [(Sprite.Player.posx, Sprite.Player.posy)], False)
    '''# modulos so that zombies come in "waves". OR escalating difficulty with ugly conditionals
    # addZombies = Var.totalKilled%5
    # screenZombies = Var.screenZombies + addZombies'''
    '''for zombie in range(Var.screenZombies - (len(Sprite.Zombies))):
        #zomx = random.randint(0, Sprite.DISPLAY_X)
        zomx = random.choice([0, Sprite.DISPLAY_X])
        zomy = random.randint(0, Sprite.DISPLAY_Y)
        zombie = Sprite.Zombie(Images.Zombie_Image, 2, (zomx, zomy), False)
        Sprite.Zombies.add(zombie)
        Sprite.spritesList.add(zombie)
    # change this for time based instead
    if Var.totalKilled == 3:
        Var.screenZombies = 2
    elif Var.totalKilled == 5:
        Var.screenZombies = 3
    elif Var.totalKilled == 10:
        Var.screenZombies = 4
    elif Var.totalKilled == 15:
        Var.screenZombies = 5 '''
    # revamped for time based: Var.addZombie = 1 if add a zombie; Var.addZombie = 0 if NOT add
    time_elapsed += 1
    if time_elapsed > wait_time:
        Var.addZombie = 1
        time_elapsed = 0
        if Var.totalKilled == 4:
            wait_time = 225
        elif Var.totalKilled == 8:
            wait_time = 200
        elif Var.totalKilled == 12:
            wait_time = 180
        elif Var.totalKilled == 15:
            wait_time = 160
    print(Var.totalKilled)
        
    for zombie in range(Var.addZombie):
        #zomx = random.randint(0, Sprite.DISPLAY_X)
        zomx = random.choice([0, Sprite.DISPLAY_X])
        zomy = random.randint(0, Sprite.DISPLAY_Y)
        zombie = Sprite.Zombie(Images.Zombie_Image, 2, (zomx, zomy), False)
        Sprite.Zombies.add(zombie)
        Sprite.spritesList.add(zombie)
        Var.addZombie = 0
        
    if Var.Health == 0:
        # Game over
        print("You died")
