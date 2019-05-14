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

questiontypes = [derivatives]
questiontype = random.choice(questiontypes)
question = random.choice(questiontype)

if questiontype == integrals:
    kind = "integral"
elif questiontype == derivatives:
    kind = "derivative"
           
response = ''


# NOTE natural log does not display well without a special function. log is displayed in base e automatically.
# integral -1/sqrt(1-x**2) returns -asin(x) NOT acos(x) error with simplify
# Beware some identities for arctrig is missing, so it may falsely say you are wrong.
# Do not use e. Sympy's syntax for e is exp() so it will be too confusing for audience.
# If you want to add more problems, add to the two lists BELOW in the function.
def show_question():
    global questiontype, question, derivatives, integrals, questiontypes , number, kind, response, waiting
    
    derivatives = [x + 3, x**2 + 5, x**2 + 6*x, tan(x), sec(x), cot(x), csc(x), acos(x), sin(x)**3, 1/x**2]
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
                Var.totalSolved += 1
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
            '''if questiontype == integrals:
                    font = pygame.font.SysFont("calibri", 30)
                    textsurface2 = font.render('+ C', False, WHITE)
                    Sprite.DISPLAY.blit(textsurface2, (400, 680)) '''              

    wait_for(60, another_question)
    show_text(response)
    if questiontype == integrals:
        font = pygame.font.SysFont("calibri", 30)
        textsurface2 = font.render('+ C', False, WHITE)
        Sprite.DISPLAY.blit(textsurface2, (500, 680))


##########################################################################################################################################################
# Calculator
text1 = ''
text2 = ''
expression = ''
def calc_question():
    global text1, text2, expression
    text = "Input expression:"

  #NOTE: log is in base e so will; both in input and output
    if Var.keyENTER:
        Var.Answer = Thing.Input2.get_text()
        try:
            #global text1, text2
            expr = Var.Answer
            expr = sympify(expr)
            deriv = diff(expr, x)
            text1 = "Derivative: " + str(deriv)
            integ = integrate(expr, x)
            text2 = "Integral: " + str(integ) + " + C"
            Var.keyENTER = False
            Thing.Input2.clear_text()
            expression = "Expression: " + str(Var.Answer)
        except:
            text1 = "Sorry, input typed wrong"
            text2 = ''
            expression = ''

    Thing.show_text(text, (430, 280), 20, (0, 0, 0))
    
    Thing.show_text(expression, (370, 180), 20, (0, 0, 0))
    Thing.show_text(text1, (370, 200), 20, (0, 0, 0))
    Thing.show_text(text2, (370, 220), 20, (0, 0, 0))
