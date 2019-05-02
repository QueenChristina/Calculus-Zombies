import pygame, sys, time, os
from pygame.locals import *
from Files import Var, Images
pygame.init()

########################################################################################################################################################
# Setting up DISPLAY and title screen
DISPLAY_X = 1024
DISPLAY_Y = 768
DISPLAY = pygame.display.set_mode ((DISPLAY_X, DISPLAY_Y))
pygame.display.set_caption('Test RPG Animations')


#########################################################################################################################################################
# importing some Sprite image files here to test. The rest are put into another file.
path = 'Walk Cycles\Player Walk Cycle'
imgPerson =[os.path.join(path, 'Side1.png'), os.path.join( path, 'Side2.png'), os.path.join(path, 'Side3.png'), os.path.join(path, 'Side4.png'),
        os.path.join(path, 'Front1.png'), os.path.join(path, 'Front2.png'), os.path.join(path, 'Front3.png'), os.path.join(path, 'Front4.png'),
        os.path.join(path, 'Back1.png'), os.path.join(path, 'Back2.png'), os.path.join(path, 'Back3.png'), os.path.join(path, 'Back4.png'),]

image_list = [imgPerson]
for u in image_list:
    for i in range (len(u)):
        u[i] = pygame.image.load(u[i])


#For a list's start to end, add an extra one to the end, as the end is NOT INCLUDED in list[start:end]        
imgPersonLeft = imgPerson [0:4]
imgPersonRight = imgPerson [0:4]
imgPersonUp = imgPerson [8:12]
imgPersonDown = imgPerson [4:8]
standleft = pygame.transform.flip(imgPerson [0], True, False)
standright = imgPerson [0]
standup = imgPerson [8]
standdown = imgPerson [4]
imgPerson = {'left': imgPersonLeft,
             'right': imgPersonRight,
             'up': imgPersonUp,
             'down': imgPersonDown,
             'standingleft': standleft,
             'standingright': standright,
             'standingup': standup,
             'standingdown': standdown}

flip_list = [imgPersonLeft]
for u in flip_list:
    for i in range (len(u)):
        u[i] = pygame.transform.flip(u[i], True, False)


#######################################################################################################################################################
# setting up Sprite class        
currentframe = 0
animationframe = 5
collideList = []
class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, imagescale, pos, run_once, *function):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.run_once = run_once
        self.done = False
        #images is a DICTIONARY of list of images lined up to a direction the object is in
        self.images = images
        self.image = self.images['left']
        
        self.rect = pygame.Rect(0, 0, 0, 0)
        # Use colliderect to prevent sprite overlap, reserve rect for the true rect of the sprite
        self.colliderect = self.rect
        # Use to detect if Player is close enough to interact with sprite; used with OPTIONAL function\
        self.interactrect = self.rect
        self.interactable = False
        self.function = function
        
        self.imagescale = imagescale
        self.dx = 0
        self.dy = 0
        self.posx = pos[0]
        self.posy = pos[1]
        self.nextpoint = 1
        self.pointcount = 0
        self.direction = 'standingleft'
        self.wasdirection = 'left'
        
        # by self.collided, I mean collided with PLAYER only
        self.collided = False
        
    def changeimage(self):
        frame = self.index
        if self.dx < 0:
            self.direction = 'left'
            self.wasdirection = 'left'
        elif self.dx > 0:
            self.direction = 'right'
            self.wasdirection = 'right'
        elif self.dy < 0:
            self.direction = 'up'
            self.wasdirection = 'up'
        elif self.dy > 0:
            self.direction = 'down'
            self.wasdirection = 'down'
        else:
            if self.wasdirection == 'left':
                # frame = 0
                 self.direction = 'standingleft'
            elif self.wasdirection == 'right':
                # frame = 1
                 self.direction = 'standingright'
            elif self.wasdirection == 'up':
                # frame = 2
                 self.direction = 'standingup'
            elif self.wasdirection == 'down':
                # frame = 3
                 self.direction = 'standingdown'
            # self.direction = 'standing'
            
        if isinstance(self.images[self.direction], list):
            if self.index > (len(self.images[self.direction]) - 1):
                self.index = 0
                frame = self.index
            self.image = self.images[self.direction][frame]
        else:
            self.image = self.images[self.direction]
            
    def imagerect(self):
        self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] / self.imagescale ), int(self.image.get_size()[1] / self.imagescale )))
        self.rect = self.image.get_rect()
        
        # feel free to change size of hitbox later, or even make it a parameter
        self.colliderect = pygame.Rect(self.rect.top, self.rect.left, 3*self.rect.width/5, self.rect.height/3)
        self.rect.topleft = (self.posx, self.posy)
        self.colliderect.midbottom = self.rect.midbottom

        self.interactrect = pygame.Rect(self.rect.top, self.rect.left, self.rect.width + 10, 50)
        self.interactrect.midtop = self.rect.midbottom

        
    def interact(self):
        if self.interactrect.colliderect(Player.colliderect):
            self.interactable = True
            if Var.keySPACE or Var.mouseCLICK:
                self.function
        else:
            self.interactable = False
        
    def moveto(self, dx, dy, points, loop):
        self.dx = dx
        self.dy = dy
        if self.posx >= (list(points)[self.pointcount][0] - abs(self.dx)) and self.posx <= (list(points)[self.pointcount][0] + abs(self.dx)):
            self.dx = 0
            if self.posy >= (list(points)[self.pointcount][1] - abs(self.dy)) and self.posy <= (list(points)[self.pointcount][1] + abs(self.dy)):
                if self.pointcount < len(list(points)) :
                    self.pointcount += self.nextpoint
                    if (self.pointcount + 1) > len(list(points)) or self.pointcount < 0:
                        if loop == True:
                            self.nextpoint *= -1
                            self.pointcount += 2*self.nextpoint
                        else:
                            self.pointcount -= self.nextpoint
        elif self.posx <= list(points)[self.pointcount][0]:
            if self.dx < 0:
                self.dx *= -1
        elif self.posx >= list(points)[self.pointcount][0]:
            if self.dx > 0:
                self.dx *= -1
        if self.posy >= (list(points)[self.pointcount][1] - abs(self.dy)) and self.posy <= (list(points)[self.pointcount][1] + abs(self.dy)):
            self.dy = 0
        elif self.posy <= list(points)[self.pointcount][1]:
            if self.dy < 0:
                self.dy *= -1
        elif self.posy >= list(points)[self.pointcount][1]:
            if self.dy > 0:
                self.dy *= -1
        self.posx += self.dx
        self.posy += self.dy
        
    def animate(self):
        global currentframe
        if self.done == True:
            # I haven't tested this out yet, so beware that this could prove problematic later...make sure you test this! Could be better to remove
            # self.run_once altogether...becareful!
            self.kill()
        else:
            if isinstance(self.images[self.direction], list):
                currentframe+= 1
                if currentframe >= animationframe:
                    currentframe = 0
                    if self.run_once == True and self.index >= (len(self.images[self.direction])-1):
                        self.done = True
                    self.index =(self.index + 1)% len(self.images[self.direction])
    def update(self):
        self.animate()
        self.changeimage()
        self.imagerect()
        self.interact()
        DISPLAY.blit(self.image, (self.posx, self.posy))

#####################################################################################################################################################
# maybe add one for background objects

#####################################################################################################################################################
# setting up special Sprite classes that need more than just being animated
# Class Object may be interactible, and are physical obstacles that cannot be walked over
class Object(Sprite):
    def __init__(self, images, imagescale, pos, run_once):
        Sprite.__init__(self, images, imagescale, pos, run_once)
        self.collisionpoint = None
        self.collision = [False] * 8
    def ifcollide(self):
        global collideList
        # it's possible collideList is unnecessary as .collide_mask() works by checking .rect collision first, and then .mask
        if self in collideList:
            # Note, for now I am not using masks for pixel perfect collisions to simplify things, but later I may.
            # if pygame.sprite.collide_mask(self, Player):
                # pygame.sprite.collide_mask() returns the first POINT the collision occurs at
                # Note, POINT is point on MASK, not position in coordinate plane
                # self.collisionpoint = (pygame.sprite.collide_mask(self, Player)[0] + self.rect.left, pygame.sprite.collide_mask(self, Player)[1] + + self.rect.top)
            if self.colliderect.colliderect(Player.colliderect):
                self.collided = True
            else:
                self.collided = False
        else:
            self.collided = False
    def obstacle(self):
        if self.collided:

            # using points to which SIDE is colliding with Player rect; BEWARE this may fail at times if one object is much larger than another
            # thanks to https://stackoverflow.com/questions/20180594/pygame-collision-by-sides-of-sprite
            # which side of Player collides with self?
            collision = [False] * 8
            collision[0] = self.colliderect.collidepoint(Player.colliderect.topleft)
            collision[1] = self.colliderect.collidepoint(Player.colliderect.topright)
            collision[2] = self.colliderect.collidepoint(Player.colliderect.bottomleft)
            collision[3] = self.colliderect.collidepoint(Player.colliderect.bottomright)

            collision[4] = self.colliderect.collidepoint(Player.colliderect.midleft)
            collision[5] = self.colliderect.collidepoint(Player.colliderect.midright)
            collision[6] = self.colliderect.collidepoint(Player.colliderect.midtop)
            collision[7] = self.colliderect.collidepoint(Player.colliderect.midbottom)

            if (collision[0] or self.collision[2] or self.collision[4]) and Player.diffx > 0:
                # LEFT side of Player touching self
                Player.posx -= Player.diffx
            if (self.collision[1] or self.collision[3] or self.collision[5]) and Player.diffx < 0:
                # RIGHT side of Player touching self
                Player.posx -= Player.diffx
            if (self.collision[0] or self.collision[1] or self.collision[6]) and Player.diffy > 0:
                # TOP side of Player touching self
                Player.posy -= Player.diffy
            if (self.collision[2] or self.collision[3] or self.collision[7]) and Player.diffy < 0:
                # BOTTOM side of Player touching self
                Player.posy -= Player.diffy
            

            # Is point on self colliding with Player rect // which side of self collides with player?
            # making corner coordinates slightly more inward to prevent corners being "sticky"
            topleft = (self.colliderect.topleft[0] + 2, self.colliderect.topleft[1] - 2)
            topright = (self.colliderect.topright[0] - 2, self.colliderect.topright[1] - 2)
            bottomleft = (self.colliderect.bottomleft[0] + 2, self.colliderect.bottomleft[1] + 2)
            bottomright = (self.colliderect.bottomright[0] - 2, self.colliderect.bottomright[1] + 2)
            self.collision[0] = Player.colliderect.collidepoint(topleft)
            self.collision[1] = Player.colliderect.collidepoint(topright)
            self.collision[2] = Player.colliderect.collidepoint(bottomleft)
            self.collision[3] = Player.colliderect.collidepoint(bottomright)

            self.collision[4] = Player.colliderect.collidepoint(self.colliderect.midleft)
            self.collision[5] = Player.colliderect.collidepoint(self.colliderect.midright)
            self.collision[6] = Player.colliderect.collidepoint(self.colliderect.midtop)
            self.collision[7] = Player.colliderect.collidepoint(self.colliderect.midbottom)

            if (self.collision[0] or self.collision[2] or self.collision[4]) and self.dx < 0:
                # LEFT of self touching player
                self.posx -= self.dx
            if (self.collision[1] or self.collision[3] or self.collision[5]) and self.dx > 0:
                # RIGHT of self touching player
                self.posx -= self.dx
            if (self.collision[0] or self.collision[1] or self.collision[6]) and self.dy < 0:
                # TOP of self touching player
                self.posy -= self.dy
            if (self.collision[2] or self.collision[3] or self.collision[7]) and self.dy > 0:
                # BOTTOM of self colliding with any of player
                self.posy -= self.dy
            
    def update(self):
        self.animate()
        self.changeimage()
        self.imagerect()
        self.ifcollide()
        self.obstacle()
        self.interact()
        DISPLAY.blit(self.image, (self.posx, self.posy))

        
######################################################################################################################################################
# setting up player class
class Player(Sprite):
    def __init__(self, images, imagescale, pos, run_once):
        Sprite.__init__(self, images, imagescale, pos, run_once)
        self.diffx = 0
        self.diffy = 0

    def move(self):
        # made this look uglier to make prevention of overlaping sprites easier. originally had no self.diff; directly added or substracted self.dx from
        # self.posx 
        if Var.keyDOWN:
            self.direction = 'down'
            self.wasdirection = 'down'
            self.diffy = self.dy
        elif Var.keyUP:
            self.direction = 'up'
            self.wasdirection = 'up'
            self.diffy = -self.dy
        else:
            self.diffy = 0
        if Var.keyLEFT:
            self.direction = 'left'
            self.wasdirection = 'left'
            self.diffx = -self.dx
        elif Var.keyRIGHT:
            self.direction = 'right'
            self.wasdirection = 'right'
            self.diffx = self.dx
        elif not (Var.keyDOWN or Var.keyUP):
            self.direction = 'standing'
            self.diffx = 0
        else:
            self.diffx = 0
        self.posx += self.diffx
        self.posy += self.diffy
    def playerimage(self):
        frame = self.index
        if self.direction == 'standing':
            if self.wasdirection == 'left':
                self.direction = 'standingleft'
            elif self.wasdirection == 'right':
                self.direction = 'standingright'
            elif self.wasdirection == 'up':
                self.direction = 'standingup'
            elif self.wasdirection == 'down':
                self.direction ='standingdown'
        if isinstance(self.images[self.direction], list):
            if self.index > (len(self.images[self.direction]) - 1):
                self.index = 0
                frame = self.index
            self.image = self.images[self.direction][frame]
        else:
            self.image = self.images[self.direction]
    def iscollide(self, group):
        global collideList        
        collideList = pygame.sprite.spritecollide(self, group, False)
    def update(self):
        self.move()
        self.playerimage()
        self.animate()
        self.imagerect()
        self.iscollide(objList)
        DISPLAY.blit(self.image, (self.posx, self.posy))        

#######################################################################################################################################################
# initializing all Sprites
objList = pygame.sprite.Group()

# excluding background sprites
spritesList = pygame.sprite.Group()

Player = Player(imgPerson, 1 , (500, 500), False)
Player.dx = 3
Player.dy = 3

objList.add()
spritesList.add(Player)

# To draw things in order by ascending y value
def drawSprites(spriteslist):
    orderedList = sorted(spriteslist, key = lambda a: a.rect.bottom)
    pygame.sprite.Group(orderedList).draw(DISPLAY)
