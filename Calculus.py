import sympy, random
from sympy import *
x, y = symbols("x y")

'''
str_expression = "tan(x) + 2"
# Beware sympify turns str to expression, but takes a long time
expression = sympify (str_expression)
answer = expression.subs(x, 3)
print (answer)

derivative = diff(expression, x)
print(derivative)

# sympy does NOT add constant of integration, add it yourself
integral = integrate(expression, x)
integral = str(integral) + " + C"
print(integral)

# limit(f(x), x, x0, optional "+" or "-" for left/right side) where the limit's x goes to x0. oo represents infinity
limit = limit(expression, x, oo)
print(limit)

# To test for equality of two equations
expr1 = 1 + tan(x)
expr2 = sin(x)/cos(x) + 1
# To see if equal, subtract one from the other and simplify; if equal to 0, the two eq are equal
equivalence = simplify(expr1 - expr2)
print(equivalence)

# If you forget a paranthesis...
str_expression = "tan(x + 2"
try:
    expression = sympify (str_expression)
    answer = expression.subs(x, 3)
    print (answer)
except:
    print("Input wrong. Maybe you forgot a paranthesis or typed wrong.")
'''

'''
print("Try an expression. Use asin(x) if arcsin(x) and ** for exponents. Use * for ALL multiplications, even for constants with variables. Use only x for variable. ")
expr = input()
try:
    expr = sympify(expr)
    deriv = diff(expr, x)
    print ("derivative is", deriv)
    integ = integrate(expr, x)
    print("integral is", integ)
except:
    print("Sorry, input typed wrong")
'''

while True:
    derivatives = [x + 3, x**2 + 5, x**2 + 6*x, tan(x), sec(x)]
    integrals = [x + 5, x + 2, 1/(1 + x**2)]
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
