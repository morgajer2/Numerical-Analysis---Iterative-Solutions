from random import randrange

from sympy import *

x = Symbol('x')


def newton_raphson(f, start_point, end_point, epsilon=0.0001):
    xr = (end_point - start_point) / 2 + start_point
    xr1 = xr - (float(f.subs(x, xr)) / float(diff(f).subs(x, xr)))
    count = 1
    while abs(float(f.subs(x, xr))) > epsilon and abs(xr1 - xr) > epsilon:
        xr = xr1
        try:
            xr1 = xr - (float(f.subs(x, xr)) / float(diff(f).subs(x, xr)))
        except:
            if float(diff(f).subs(x, xr))==0:
                return (xr,count)
        count += 1
    return (xr1, count)


def secant_method(f, start_point, end_point, epsilon=0.0001):
    xr0 = (end_point - start_point) / 2 + start_point  # xr-1
    xr = (end_point - start_point) / 2 + epsilon + start_point  # xr
    try:
        xr1 = (xr0 * float(f.subs(x, xr)) - xr * float(f.subs(x, xr0))) / (
                float(f.subs(x, xr)) - float(f.subs(x, xr0)))  # xr+1
    except:
        if float(f.subs(x, xr)) ==0:
            return xr
        elif float(f.subs(x, xr0)) ==0:
            return xr0
    count = 1
    while abs(float(f.subs(x, xr))) > epsilon:
        xr = xr1
        try:
            xr1 = (xr0 * float(f.subs(x, xr)) - xr * float(f.subs(x, xr0))) / (
                    float(f.subs(x, xr)) - float(f.subs(x, xr0)))  # xr+1
        except:
            if float(f.subs(x, xr)) == 0:
                return (xr,count)
            elif float(f.subs(x, xr0)) == 0:
                return (xr0,count)
        count += 1
    return (xr1, count)


def mainFunc(f, start_point, end_point, epsilon=0.0001):
    x0 = start_point
    roots_secant = list()
    roots_newton = list()
    while x0<end_point:
        ay = float(f.subs(x, x0))
        by = float(f.subs(x, x0 + 1))
        if ay * by < 0:  # Suspicious root
            roots_secant.append(secant_method(f, x0, x0 + 1))
            roots_newton.append(newton_raphson(f, x0, x0 + 1))
        elif ay==0 and (x0,0) not in roots_secant:
            roots_secant.append((x0,0))
            roots_newton.append((x0, 0))
        elif by==0:
            roots_secant.append((x0+1, 0))
            roots_newton.append((x0+1,0))
        x0 += 1
    # printing:
    if not roots_secant and not roots_newton:
        print("no roots found")
    else:
        print("\nby secant method: ")
        for t in roots_secant:
            print("number of iterations: " + str(t[1]) + " root: " + str(t[0]))
        print("\nby newton_raphson: ")
        for t in roots_newton:
            print("number of iterations: " + str(t[1]) + " root: " + str(t[0]))
    return (roots_secant, roots_newton)


# Solve quadratic equation like, example : x ^ 2?2 = 0
f2 = (x ** 2) - 5 * x + 6
f3 = 4 * (x ** 3) - 48 * x + 5

print("func: 4 * (x ** 3) - 48 * x + 5")
mainFunc(f3, 2, 6)
print("func: x ** 2 - 5 * x + 6 ")
mainFunc(f2, 0, 6)