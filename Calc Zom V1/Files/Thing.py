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
    Sprite.DISPLAY.blit(Input.get_surface(), (80, 620))
    # Text = Input.get_text()
    if Var.keyENTER:
        Var.Answer = Input.get_text()

    Sprite.DISPLAY.blit(text_box_status, (750,10))
    text_ammo =  str(Var.Ammo) + " power"
    text_health = str(Var.Health) + " health"
    show_text(text_ammo,  (780, 30), 30, WHITE)
    show_text(text_health,  (780, 60), 30, WHITE)

###########################################################################################################################################################

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

desk = pygame.image.load(os.path.join('Stuff', 'Desk with Chair.png'))
desk = Images.autodict(desk, desk, desk, desk, desk, desk)
#desk = Sprite.Object(desk, 2/3, (820, 350), False)
desk_positions = [(850, 500), (850, 350), (850, 200),
                  (250, 500), (250, 350), (250, 200),
                  (50, 500), (50, 350), (50, 200),
                  (650, 500), (650, 350), (650, 200),
                  (450, 500), (450, 350), (450, 200)]

plant = pygame.image.load(os.path.join('Stuff', 'Plant.png'))
plant = Images.autodict(plant, plant, plant, plant, plant, plant)
plant = Sprite.Object(plant,1/2, (630, 60), False)
def shoot_zombies():
    if Var.set_up_class == True:
        global time_elapsed, wait_time, total_time_elapsed

        for zombie in Sprite.Zombies:
            zombie.kill()

        Var.Answer = None
        Var.Health = 20
        Var.Ammo = 5
        Var.screenZombies = 1
        Var.totalKilled = 0
        Var.addZombie = 1
        Var.totalSolved = 0

        Var.mouseDOWNPOS = (0, 0)
        Var.mouseDOWN = False

        Sprite.Player.posx = int(Sprite.DISPLAY_X/2 - 8)
        #Sprite.Player.posy = int(Sprite.DISPLAY_Y/2)
        Sprite.Player.posy = 120
        Sprite.Player.wasdirection = 'down'
                              
        time_elapsed = 0
        wait_time = 250
        total_time_elapsed = 0
        Sprite.objList.add(classroomwall)
        Sprite.spritesList.add(classroomwall)

        Sprite.objList.add(plant)
        Sprite.spritesList.add(plant)
        
        for pos in range(len(desk_positions)):
            table = Sprite.Object(desk, 2/3, desk_positions[pos], False)
            Sprite.objList.add(table)
            Sprite.spritesList.add(table)
        
        Var.set_up_class = False
        
    Sprite.DISPLAY.blit(classroom, (0,0))

    Sprite.objList.update()
    
    Sprite.Player.update()
    Sprite.Zombies.update()
    
    Sprite.drawSprites(Sprite.spritesList)
    Sprite.Bullets.update()

    
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
        zombie = Sprite.Zombie(Images.Zombie_Image, 5/2, (zomx, zomy), False)
        Sprite.Zombies.add(zombie)
        Sprite.spritesList.add(zombie)
        Var.addZombie = 0
        
    if Var.Health <= 0:
        # Game over
        Var.in_class = False
        Var.you_died = True
        Var.set_up_died = True

###############################################################################################################################

gameover = pygame.image.load(os.path.join('Stuff', 'GameOver.png'))
gameover = pygame.transform.scale(gameover, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))
def you_died():
    if Var.set_up_died == True:
        global time_elapsed, wait_time
        wait_time = 10
        time_elapsed = 0

        Var.mouseDOWN = False
        
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

    if Var.totalSolved >= 18:
        grade = "A-"
        synopsis = "Almost there!"
    elif Var.totalSolved >= 13:
        grade = "B"
        synopsis = "Nice job!"
    elif Var.totalSolved >= 9:
        grade = "B-"
        synopsis = "Asian Fail. But not bad. :)"
    elif Var.totalSolved >= 7:
        grade = "C-"
        synopsis = "Pass...I guess."
    elif Var.totalSolved >= 3:
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

###############################################################################################################################
# very important teacher
teacher = pygame.image.load(os.path.join('Stuff', 'Mr.Zomboy.png'))
#teacher = pygame.transform.scale(teacher, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))
teacher = pygame.transform.scale2x(teacher)
teacher_rect = teacher.get_rect()

skip = pygame.image.load(os.path.join('Stuff', 'Skip Hand.png'))
skip = pygame.transform.scale2x(skip)
skip_rect = skip .get_rect()

tutorial = Images.listimages('Tutorial', 16)

def tutorial_class():
    if Var.set_up_tutorial == True:
        global tut_num, teacherposy, teacherpos_sign, teachermove, skip_posy
        tut_num = 0

        teacherposy = 200
        teacherpos_sign = -1
        teachermove = 5

        skip_posy = 0
        
        Var.mouseDOWN = False
        Var.set_up_tutorial = False

    Sprite.DISPLAY.blit(classroom, (0,0))
    
    Sprite.DISPLAY.blit(teacher, (0,Sprite.DISPLAY_Y - teacher_rect.height + int(teacherposy)))
    teacher_rect.topleft = (0,Sprite.DISPLAY_Y - teacher_rect.height + int(teacherposy))

    Sprite.DISPLAY.blit(skip, (Sprite.DISPLAY_X - skip_rect.width, -13 + skip_posy))
    skip_rect.topleft = (Sprite.DISPLAY_X - skip_rect.width, -13 + skip_posy)

    Sprite.DISPLAY.blit(tutorial[tut_num], (130,100))

    if teacherposy <= 10 and teacherposy >= 0:
        teacherpos_sign = 0.5
        teachermove = 1
    elif teacherposy <= 60 and teacherposy >= 50:
        teacherpos_sign = -1
        
    teacherposy += teachermove * teacherpos_sign

    if tut_num == 0:
        show_text("Click to move on >>>", (750, 730), 30, (220, 50, 60))

    if Var.mouseDOWN == True:
        if tut_num >= len(tutorial) - 1:
            Var.set_up_class = True
            Var.in_class = True
            Var.tutorial_class = False
        else:
            tut_num += 1
            
            Var.mouseDOWN = False

        if skip_rect.collidepoint(Var.mouseDOWNPOS):
            if tut_num <= 14:
                tut_num = 15
            else:
                Var.set_up_class = True
                Var.in_class = True
                Var.tutorial_class = False

    if skip_rect.collidepoint(Var.mousePOS):
        skip_posy = 13
    else:
        skip_posy = 0                
    
###########################################################################################################################################################
menu = pygame.image.load(os.path.join('Stuff', 'Menu.png'))
menu = pygame.transform.scale(menu, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))

copyrt = pygame.image.load(os.path.join('Stuff', 'Copyright.png'))
#copyrt = pygame.transform.scale(copyrt, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))

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

calc_sign = pygame.image.load(os.path.join('Stuff', 'Calculator.png'))
calc_sign = pygame.transform.scale2x(calc_sign)
calc_sign_rect = calc_sign.get_rect()

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
        Var.mouseDOWN = False
        Var.set_up_menu = False

    # background
    Sprite.DISPLAY.blit(menu, (0,0))
    Sprite.DISPLAY.blit(copyrt, (400,700))

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

    # title animation
    titley += 0.4 * title_sign
    if titley <= 10 and titley >= 9:
        title_sign = -1
    elif titley <= 1 and titley >= 0:
        title_sign = 1

    # hover animation
    if class_sign_rect.collidepoint(Var.mousePOS):
        pygame.draw.rect(Sprite.DISPLAY, (220, 80, 100), class_sign_rect, 0)
    elif learn_sign_rect.collidepoint(Var.mousePOS):
        pygame.draw.rect(Sprite.DISPLAY, (220, 80, 100), learn_sign_rect, 0)
    elif calc_sign_rect.collidepoint(Var.mousePOS):
        pygame.draw.rect(Sprite.DISPLAY, (220, 80, 100), calc_sign_rect, 0)


    # draw signs       
    Sprite.DISPLAY.blit(title, (20 , int(40 + titley)))
    Sprite.DISPLAY.blit(hand, (0,0))

    Sprite.DISPLAY.blit(class_sign, (650,400))
    class_sign_rect.topleft = (650,400)
    
    Sprite.DISPLAY.blit(learn_sign, (10,400))
    learn_sign_rect.topleft = (10,400)

    Sprite.DISPLAY.blit(calc_sign, (10,550))
    calc_sign_rect.topleft = (10,550)

    time_elapsed += 1
    if time_elapsed > wait_time:        
       # Place ALL button/mouse click detecting in here to that no accidental clicking before reading takes place 
        if Var.mouseDOWN == True:
            if class_sign_rect.collidepoint(Var.mouseDOWNPOS):
                #Var.set_up_class = True
                #Var.in_class = True
                Var.set_up_tutorial = True
                Var.tutorial_class = True
                Var.menu = False
            elif learn_sign_rect.collidepoint(Var.mouseDOWNPOS):
                Var.set_up_lesson = True
                Var.lesson = True
                Var.menu = False
            elif calc_sign_rect.collidepoint(Var.mouseDOWNPOS):
                Var.set_up_calculator = True
                Var.calculator = True
                Var.menu = False
                
###########################################################################################################################################################

Input2 =  InputText.TextInput(
            initial_string=" ",
            font_family="Calibri",
            font_size= 20,
            antialias = True,
            text_color= (0, 0, 0),
            cursor_color= (0, 0, 0),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35)
screen = pygame.image.load(os.path.join('Stuff', 'TI 83 Screen.png'))
screen = pygame.transform.scale2x(screen)

Box = pygame.image.load(os.path.join('Stuff', 'Notes Box.png'))
Box = pygame.transform.scale(Box, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y + 70))

def calc_screen():
    #Sprite.DISPLAY.blit(screen, (300,30))
    text = "Question"
    show_text(text, (500, 140), 20, (0, 0, 0))

calc = pygame.image.load(os.path.join('Stuff', 'TI 83.png'))
calc = pygame.transform.scale2x(calc)
calc_rect = calc.get_rect()
def calculator():
    if Var.set_up_calculator == True:
        global calcy, calcwait_time, calctime_elapsed
        Var.mouseDOWNPOS = (0, 0)
        Var.mouseDOWN = False
        calcy = 300

        calcwait_time = 10
        calctime_elapsed = 0
        
        Var.set_up_calculator = False
    Sprite.DISPLAY.blit(menu, (0,0))

    Sprite.DISPLAY.blit(calc, (300,calcy))
    calc_rect.topleft = (300,calcy)

    if calcy <= 30:
        calcy = 30
        calc_screen()
        #Sprite.DISPLAY.blit(text_box, (0, int(4*Sprite.DISPLAY_Y/5)))
        #events = pygame.event.get()        
        #Input2.update(events)
        Sprite.DISPLAY.blit(Input2.get_surface(), (450, 310))

        Calculus.calc_question()

        Sprite.DISPLAY.blit(Box, (0,-35))

        show_text("NOTE: log is in base e.", (40, 140), 20, (0, 0, 0))
        show_text("Use asin for arcsin, etc..", (40, 170), 20, (0, 0, 0))
        show_text("Use ** as exponent.", (40, 200), 20, (0, 0, 0))
        show_text("Must * coefficents to x.", (40, 230), 20, (0, 0, 0))
        show_text("(4x is illegal. 4*x is okay.)", (40, 260), 20, (0, 0, 0))
        show_text("Use exp(x) for e**x.", (40, 290), 20, (0, 0, 0))

        show_text("Everything in respect to x variable.", (40, 310), 15, (0, 0, 0))
        show_text("Other letters may be used as constants.", (40, 330), 15, (0, 0, 0))

        space = 10
        show_text("Will freeze if too hard.", (40, 350 + space), 20, (0, 0, 0))
        
        show_text("log in base 10 unavailable", (40, 380 + space), 20, (0, 0, 0))

        show_text("Click elsewhere to return.", (40, 410 + space), 20, (0, 0, 0))
        
    else:
        calcy -= 8

    events = pygame.event.get()    
    Input2.update(events)
    
    calctime_elapsed += 1
    if calctime_elapsed > calcwait_time:        
        if Var.mouseDOWN == True:
            if not calc_rect.collidepoint(Var.mouseDOWNPOS):
                Var.set_up_menu = True
                Var.calculator = False
                Var.menu = True

###########################################################################################################################################################

# teacher and skip image loaded before tutorial_class

lesson_back = pygame.image.load(os.path.join('Stuff', 'Lesson.png'))
lesson_back = pygame.transform.scale(lesson_back, (Sprite.DISPLAY_X, Sprite.DISPLAY_Y))
#lesson_back_rect = lesson_back.get_rect()

# loading up lesson dialogue boxes
hi = pygame.image.load(os.path.join('Stuff', 'Hi.png'))
hi = pygame.transform.scale2x(hi)

intro = pygame.image.load(os.path.join('Stuff', 'intro.png'))
intro = pygame.transform.scale2x(intro)

joke = pygame.image.load(os.path.join('Stuff', 'joke.png'))
joke = pygame.transform.scale2x(joke)

joke2 = pygame.image.load(os.path.join('Stuff', 'joke2.png'))
joke2 = pygame.transform.scale2x(joke2)

know = pygame.image.load(os.path.join('Stuff', 'know.png'))
know = pygame.transform.scale2x(know)

drool = pygame.image.load(os.path.join('Stuff', 'drool.png'))
drool = pygame.transform.scale2x(drool)

anyway = pygame.image.load(os.path.join('Stuff', 'anyway.png'))
anyway = pygame.transform.scale2x(anyway)


test = pygame.image.load(os.path.join('Stuff', 'test.png'))
test = pygame.transform.scale2x(test)

late = pygame.image.load(os.path.join('Stuff', 'late.png'))
late = pygame.transform.scale2x(late)

eat = pygame.image.load(os.path.join('Stuff', 'eat.png'))
eat = pygame.transform.scale2x(eat)

learn = Images.listimages('Learn', 17)

intro = [hi, intro, joke, joke2, know, drool, anyway]

end = [anyway, test, late, eat]

dialogue = intro + learn + end

def dolesson():
    if Var.set_up_lesson == True:
        global teacherposy, teacherpos_sign, teachermove, skip_posy, talk_num
        Var.mouseDOWNPOS = (0, 0)
        Var.mouseDOWN = False

        teacherposy = 200
        teacherpos_sign = -1
        teachermove = 5

        skip_posy = 0

        talk_num = 0
        
        Var.set_up_lesson = False
        
    Sprite.DISPLAY.blit(lesson_back, (0,0))
    Sprite.DISPLAY.blit(dialogue[talk_num], (100,30))

    Sprite.DISPLAY.blit(skip, (Sprite.DISPLAY_X - skip_rect.width, -13 + skip_posy))
    skip_rect.topleft = (Sprite.DISPLAY_X - skip_rect.width, -13 + skip_posy)
    
    Sprite.DISPLAY.blit(teacher, (0,Sprite.DISPLAY_Y - teacher_rect.height + int(teacherposy)))
    teacher_rect.topleft = (0,Sprite.DISPLAY_Y - teacher_rect.height + int(teacherposy))

    if teacherposy <= 10 and teacherposy >= 0:
        teacherpos_sign = 0.5
        teachermove = 1
    elif teacherposy <= 60 and teacherposy >= 50:
        teacherpos_sign = -1
        
    teacherposy += teachermove * teacherpos_sign

    if Var.mouseDOWN == True:
        if talk_num >= len(dialogue) - 1:
            Var.set_up_menu = True
            Var.lesson = False
            Var.menu = True
        else:
            talk_num += 1
            
            Var.mouseDOWN = False
            
        if skip_rect.collidepoint(Var.mouseDOWNPOS):
            Var.set_up_menu = True
            Var.lesson = False
            Var.menu = True

    if skip_rect.collidepoint(Var.mousePOS):
        skip_posy = 13
    else:
        skip_posy = 0    

