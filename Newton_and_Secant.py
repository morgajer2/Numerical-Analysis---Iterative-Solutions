from sympy import *
x = Symbol('x')

def Newton_Raphson(f, start_point, end_point, epsilon=0.0001):
    pass

def secant_method(f, start_point, end_point, epsilon=0.0001):
    pass






# Solve quadratic equation like, example : x ^ 2?2 = 0
f = x**2 -2
ans5 = solve(x**2 - 2, x)
print("roots are : ", ans5)
print(f.subs(x,5))

