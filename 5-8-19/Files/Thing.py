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

def show_text(text, pos, size, color):
    # small_font = pygame.font.Font("PixelFont.ttf", 35)
    #text_surface = small_font.render(text, False, (255, 255, 255))
    font = pygame.font.SysFont("calibri", size)
    textsurface = font.render(str(text), False, color)
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
    text_ammo =  str(Var.Ammo) + " power"
    text_health = str(Var.Health) + " health"
    show_text(text_ammo,  (780, 30), 30, WHITE)
    show_text(text_health,  (780, 60), 30, WHITE)


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
def shoot_zombies():
    if Var.set_up_class == True:
        global time_elapsed, wait_time, total_time_elapsed

        for zombie in Sprite.Zombies:
            zombie.kill()

        Var.Answer = None
        Var.Health = 30
        Var.Ammo = 8
        Var.screenZombies = 1
        Var.totalKilled = 0
        Var.addZombie = 1
        Var.totalSolved = 0
        
        time_elapsed = 0
        wait_time = 250
        total_time_elapsed = 0
        Sprite.objList.add(classroomwall)
        Sprite.spritesList.add(classroomwall)
        Var.set_up_class = False
        
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
    total_time_elapsed += 1
    if time_elapsed > wait_time:
        Var.addZombie = 1
        time_elapsed = 0
        if total_time_elapsed >= 1500:
            wait_time = 155
        elif total_time_elapsed >= 1300:
            wait_time = 160
        elif total_time_elapsed >= 1100:
            wait_time = 180
        elif total_time_elapsed >= 800:
            wait_time = 200
        elif total_time_elapsed >= 500:
            wait_time = 225
        '''if Var.totalKilled == 4:
            wait_time = 225
        elif Var.totalKilled == 8:
            wait_time = 200
        elif Var.totalKilled == 12:
            wait_time = 180
        elif Var.totalKilled == 15:
            wait_time = 160'''
        
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
        Var.in_class = False
        Var.you_died = True
        Var.set_up_died = True

gameover = pygame.image.load(os.path.join('Stuff', 'GameOver.png'))
gameover = pygame.transform.scale(gameover, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))
def you_died():
    if Var.set_up_died == True:
        global time_elapsed, wait_time
        wait_time = 10
        time_elapsed = 0
        Var.set_up_died = False        

    Sprite.DISPLAY.blit(gameover, (0,0))
    
    text = "YOU DISAPPOINTED MR.ZOMBIE!"
    show_text(text, (60, 100), 70, (255, 90, 100))
    show_text("Click anywhere to return to menu.", (310, 200), 25, (255, 255, 255))

    score = "You impressed " + str(Var.totalKilled) + " zombies."
    score2 = "You solved " + str(Var.totalSolved) + " problems."
    score3 = "You lasted " + str(int(total_time_elapsed/30)) + " seconds."

    height = -100
    show_text(score, (int(Sprite.DISPLAY_X/2 - 220), 400 + height), 40, (255, 195, 200))
    show_text(score2, (int(Sprite.DISPLAY_X/2 - 200), 450 + height), 40, (255, 195, 200))
    show_text(score3, (int(Sprite.DISPLAY_X/2 - 200), 500 + height), 40, (255, 195, 200))
    show_text("_________________________________________________", (20, 530 + height), 40, (255, 195, 200))

    if Var.totalSolved >= 13:
        grade = "A-"
        synopsis = "Almost there!"
    elif Var.totalSolved >= 9:
        grade = "B-"
        synopsis = "Asian Fail."
    if Var.totalSolved >= 7:
        grade = "C-"
        synopsis = "Pass...I guess."
    if Var.totalSolved >= 3:
        grade = "D+"
        synopsis = "Better than D-!"
    else:
        grade = "F"
        synopsis = "Did you even try? :("
    grade = "Grade: " + grade
    synopsis = "Synopsis: " + synopsis
    show_text(grade, (int(Sprite.DISPLAY_X/2 + 80), 580 + height), 40, (255, 90, 100))
    show_text(synopsis, (int(Sprite.DISPLAY_X/2 - 230), 640 + height), 40, (200, 195, 255))

    time_elapsed += 1
    if time_elapsed > wait_time: 
        if Var.mouseDOWN == True:
            Var.menu = True
            Var.set_up_menu = True
            Var.you_died = False

menu = pygame.image.load(os.path.join('Stuff', 'Menu.png'))
menu = pygame.transform.scale(menu, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))

hand = pygame.image.load(os.path.join('Stuff', 'Hand.png'))
hand = pygame.transform.scale(hand, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))

title = pygame.image.load(os.path.join('Stuff', 'Title Crop.png'))
title_rect = title.get_rect()

class_sign = pygame.image.load(os.path.join('Stuff', 'Go to Class.png'))
class_sign = pygame.transform.scale2x(class_sign)
class_sign_rect = class_sign.get_rect()

learn_sign = pygame.image.load(os.path.join('Stuff', 'Learn.png'))
learn_sign = pygame.transform.scale2x(learn_sign)
learn_sign_rect = learn_sign.get_rect()

def do_menu():
    global title
    if Var.set_up_menu == True:
        global time_elapsed, wait_time, title_degree, title_scale, title_sign, title_time_elapsed, titley 
        title_scale = 2
        title_sign = 1
        title_time_elapsed = 0
        titley = 0
        
        wait_time = 10
        time_elapsed = 0
        title_degree = 0
        Var.mouseDOWNPOS = (0, 0)
        Var.set_up_menu = False

    Sprite.DISPLAY.blit(menu, (0,0))

    #title = pygame.transform.rotate(title, title_degree)
    #title_degree += 1
    '''title_time_elapsed += 1
    if title_time_elapsed > wait_time:
        title_scale += 0.2 * title_sign
        title_time_elapsed = 0
        if title_scale <= 3.5 and title_scale >= 3:
            title_sign = -1
        elif title_scale <= 1.5 and title_scale >= 1:
            title_sign = 1'''
    '''title_scale += 0.2 * title_sign
    title_time_elapsed = 0
    if title_scale <= 3.5 and title_scale >= 3:
        title_sign = -1
    elif title_scale <= 1.5 and title_scale >= 1:
        title_sign = 1
    title_rect2 = title.get_rect()
    title = pygame.transform.scale(title, (int(title_rect.width*title_scale/3), int(title_rect.height*title_scale/3)))
    
    Sprite.DISPLAY.blit(title, (500 - (title_rect2.width/2), 300 - int(title_rect2.height/2)))'''

    titley += 0.4 * title_sign
    if titley <= 10 and titley >= 9:
        title_sign = -1
    elif titley <= 1 and titley >= 0:
        title_sign = 1
            
    Sprite.DISPLAY.blit(title, (20 , int(40 + titley)))
    Sprite.DISPLAY.blit(hand, (0,0))

    Sprite.DISPLAY.blit(class_sign, (600,500))
    class_sign_rect.topleft = (600,500)
    
    Sprite.DISPLAY.blit(learn_sign, (50,500))
    learn_sign_rect.topleft = (50,500)

    time_elapsed += 1
    if time_elapsed > wait_time:        
       # Place ALL button/mouse click detecting in here to that no accidental clicking before reading takes place 
        if Var.mouseDOWN == True:
            if class_sign_rect.collidepoint(Var.mouseDOWNPOS):
                Var.set_up_class = True
                Var.in_class = True
                Var.menu = False
            elif learn_sign_rect.collidepoint(Var.mouseDOWNPOS):
                pass
        
