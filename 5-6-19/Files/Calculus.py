import sympy, random, pygame
from sympy import *
from pygame.locals import *
from Files import Var, Sprite, Thing

x, y = symbols("x y")

pygame.font.init()

WHITE = (255, 255, 255)
def show_text(text):
    # small_font = pygame.font.Font("PixelFont.ttf", 35)
    #text_surface = small_font.render(text, False, (255, 255, 255))
    font = pygame.font.SysFont("calibri", 30)
    textsurface = font.render(str(text), False, WHITE)
    Sprite.DISPLAY.blit(textsurface, (50, 640))

frames = 0
waiting = 'done'
def wait_for(time, function):
    global waiting, frames
    if waiting == 'not done':
        if frames > time:
            frames = 0
            function()
            waiting = 'done'
        else:
            frames += 1
    else:
        pass

def another_question():
    global questiontype, question, derivatives, integrals, questiontypes , number, kind
    questiontypes = [derivatives, integrals]
    questiontype = random.choice(questiontypes)
    question = random.choice(questiontype)
    Thing.Input.clear_text()

derivatives = [x + 3, x**2 + 5, x**2 + 6*x, tan(x), sec(x)]
integrals = [x + 5, x + 2, 1/(1 + x**2)]

questiontypes = [derivatives, integrals]
questiontype = random.choice(questiontypes)
question = random.choice(questiontype)

if questiontype == integrals:
    kind = "integral"
elif questiontype == derivatives:
    kind = "derivative"
            
response = ''

# NOTE natural log does not work without a special function.
# integral -1/sqrt(1-x**2) returns -asin(x) NOT acos(x) error with simplify
# Do not use e. Sympy's syntax for e is exp() so it will be too confusing for audience.
def show_question():
    global questiontype, question, derivatives, integrals, questiontypes , number, kind, response, waiting
    
    derivatives = [x + 3, x**2 + 5, x**2 + 6*x, tan(x), sec(x), acos(x), sin(x)**3]
    integrals = [x + 5, 3*x**2 + 2, 1/(1 + x**2), 1, sec(x)**2, csc(x)**2, sin(x), cos(x), sec(x)*tan(x), csc(x)*cot(x), 1/sqrt(1-x**2)]

    rightorwrong = False
    
    if Var.keyENTER:
        
        try:
            answer = Var.Answer
            answer = sympify(answer)
            if kind == "derivative":
                questans = diff(question, x)
            elif kind == "integral":
                questans = integrate(question, x)
                
            equivalence = simplify(answer - questans)
            
            if equivalence == 0:
                # print("Correct. It was", questans)
                response = "Correct. It was " + str(questans)
                Var.Ammo += 3
                Var.keyENTER = False
                
            else:
                # print("wrong. It was", questans)
                response = "Wrong. It was " + str(questans)
                
            waiting = 'not done'

        except:
            #print("Sorry, input typed wrong. Remember to use ** for exponents and multiply everything with * .")
            #print("Use asin(x) instead of arcsin(x) and don't forget paranthesis. ")
            response = "Sorry, input typed wrong."

            waiting = 'not done'

    else:
        if questiontype == integrals:
            kind = "integral"
        elif questiontype == derivatives:
            kind = "derivative"
            
        if waiting == 'done':
            response = 'Solve for ' + kind + ' of ' + str(question)

    wait_for(60, another_question)
    show_text(response)

