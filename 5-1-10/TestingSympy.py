import sympy, random, pygame
from sympy import *

x, y = symbols("x y")

e = E
while True:
    derivatives = [e**x]
    integrals = [e**x]
    questiontypes = [derivatives, integrals]
    questiontype = random.choice(questiontypes)
    question = random.choice(questiontype)
    if questiontype == integrals:
        kind = "integral"
    elif questiontype == derivatives:
        kind = "derivative"
    print("Solve for", kind, " of", str(question))
    answer = input()
    try:
        answer = sympify(answer)
        if kind == "derivative":
            questans = diff(question, x)
        elif kind == "integral":
            questans = integrate(question, x)
        equivalence = simplify(answer - questans)
        if equivalence == 0:
            print("Correct. It was", questans)
        else:
            print("wrong. It was", questans)
    except:
        print("Sorry, input typed wrong. Remember to use ** for exponents and multiply everything with * .")
        print("Use asin(x) instead of arcsin(x) and don't forget paranthesis. ")
