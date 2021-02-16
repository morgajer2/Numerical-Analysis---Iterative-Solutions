from math import e

from sympy import *


x = Symbol('x')


def simpson(f, a, b, n, epsilon=0.000001):
    """

    :param f:
    :param a:
    :param b:
    :param n: number of ranges (number of simpsons)
    :param epsilon:
    :return:
    """
    if n % 2 != 0:
        n = n - 1
    print("n:" + str(float(n)))
    h = (b - a) / n
    print("h:" + str(float(h)))
    sum = f.subs(x, a)
    j = 4
    x0 = a + h
    print("i:" + str(0) + "  x:" + str(float(x0)) + "  f(x):" + str(float(f.subs(x, x0))))
    for i in range(1, n):
        sum += j * f.subs(x, x0)
        x0 += h
        if j == 4:
            j = 2
        else:
            j = 4
        print("i:" + str(i) + "  x:" + str(float(x0)) + "  f(x):" + str(float(f.subs(x, x0))))
    sum += f.subs(x, b)
    return float((1 / 3) * h * sum)

def trapeze(f, k, a, b): # TODO: fix trapeze methood!!!
    """

    :param f:
    :param k:
    :param a:
    :param b:
    :return:
    """
    h = (b - a)/k
    X0 = a
    sum = (1/(2**k))*b
    sum_new = 0
    for i in range(1,k):
        X0 = X0 + h
        sum_new += f.subs(x, X0)
    sum_new = 2 * sum_new
    sum = sum * (f.subs(x, a) + f.subs(x, b) + sum_new)
    return sum


def romberg(f, a, b, epsilon=0.000001):
    """

    :param f:
    :param a:
    :param b:
    :param epsilon:
    :return:
    """
    r = dict()
    r[1, 1] = trapeze(f, 1, a, b)
    r[2, 1] = trapeze(f, 2, a, b)
    r[2, 2] = r[2, 1] + (1 / 3) * (r[2, 1] - r[1, 1])
    i = 2

    def rom(i, j):
        if j==1:
            r[i,j] = trapeze(f, i, a, b)
            return
        if (i, j - 1) not in r:
            rom(i, j - 1)
        if (i - 1, j-1) not in r:
            rom(i - 1, j)
        r[i,j] = r[i, j - 1] + ((1 / (4 ** (j - 1) - 1)) * (r[i, j - 1] - r[i - 1, j - 1]))

    while abs(r[i, i] - r[i - 1, i - 1]) > epsilon:
        rom(i + 1, i + 1)
        i += 1
    return r[i, i]




"""
f = (sin(x**4+5*x-6))/(2*(2.71**((-2)*x+5)))
print(simpson(f, -0.5, 0.5))

"""
f17 = ((x**2)*(e**(-x**2-5*x-3)))*(3*x-1)
print("func: " + str(f17))
#print(simpson(f17, 0.5,1,5))
print(float(romberg(sin(x),0,pi)))
