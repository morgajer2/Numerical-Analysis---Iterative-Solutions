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
    print("\nmiddle results:")
    sum = f.subs(x, a)
    func = "f(a)"
    j = 4
    x0 = a + h
    print("i:" + str(0) + "  x:" + str(float(x0)) + "  f(x):" + str(float(f.subs(x, x0))))
    for i in range(1, n):
        sum += j * f.subs(x, x0)
        func += " + " + str(j) + "*f(x" + str(i) + ")"
        x0 += h
        if j == 4:
            j = 2
        else:
            j = 4
        print("i:" + str(i) + "  x:" + str(float(x0)) + "  f(x):" + str(float(f.subs(x, x0))))
    sum += f.subs(x, b)
    func += " + f(b)"
    func = "(1/3)*h * (" + func + ")"
    return float((1 / 3) * h * sum), func


def trapeze(f, k, a, b):  # TODO: fix trapeze methood!!!
    """

    :param f:
    :param k:
    :param a:
    :param b:
    :return:
    """
    h = (b - a) / (2**k)
    X0 = a
    sum = h
    sum_new = 0
    nos=str(h)+"*"+"["+"0.5*f("+str(a)+")"+"+"

    for i in range(0, (2**k)-1):
        X0 = X0 + h
        sum_new += f.subs(x, X0)
        nos+="f("+str(X0)+")"+"+"
    nos+="f("+str(b)+")"+"]"
    sum = sum * (0.5*f.subs(x, a) + 0.5*f.subs(x, b) + sum_new)
    nos+="="+str(float(sum))
    return sum,nos


def romberg(f, a, b, epsilon=0.000001):
    """

    :param f:
    :param a:
    :param b:
    :param epsilon:
    :return:
    """
    r = dict()
    r2= dict()
    r[0, 0],r2[0,0] = trapeze(f, 0, a, b)
    r[1, 0],r2[1,0] = trapeze(f, 1, a, b)
    r[1, 1] = r[1, 0] + (1 / 3) * (r[1, 0] - r[0, 0])
    r2[1,1]="r[1, 0] + (1 / 3) * (r[1, 0] - r[0, 0])"+"="+str(float(r[1,1]))
    i = 1

    def rom(i, j):
        if j == 0:
            r[i, j],r2[i,j] = trapeze(f, i, a, b)
            return
        if (i, j - 1) not in r:
            rom(i, j - 1)
        if (i - 1, j - 1) not in r:
            rom(i - 1, j)
        r[i, j] = r[i, j - 1] + ((1 / (4 ** (j) - 1)) * (r[i, j - 1] - r[i - 1, j - 1]))
        r2[i,j]="r["+str(i)+","+str(j - 1)+"] +"+str((1 / (4 ** (j) - 1)) )+"* (r["+str(i)+","+str(j - 1)+"] - r["+str(i - 1)+", "+str(j - 1)+"]))="+str(float(r[i,j]))

    while abs(r[i, i] - r[i - 1, i - 1]) > epsilon:
        rom(i + 1, i + 1)
        i += 1
    return r[i, i],r2


"""
f9 = (sin(x ** 4 + 5 * x - 6)) / (2 * (e ** (-2 * x + 5)))
r,r2=romberg(f9,-0.5,0.5)
for i in r2:
    print("i="+str(i[0])+" j="+str(i[1])+" "+r2[i])
print("\nresult:"+str(r))
"""
f17 = ((x**2)*(e**(-x**2-5*x-3)))*(3*x-1)
r,r2=romberg(f17,0.5,1)
for i in r2:
    print("i="+str(i[0])+" j="+str(i[1])+" "+r2[i])
print("\nresult:"+str(r))



"""
f9 = (sin(x ** 4 + 5 * x - 6)) / (2 * (e ** (-2 * x + 5)))
a = -0.5
b = 0.5
print("func: " + str(f9))
sum, func = simpson(f9, a, b, 6)
print("\nResult:\nintegrate " + str(f9) + " dx from x=" + str(a) + " to " + str(b) + " = \n" + func + " = " + str(sum))


f17 = ((x**2)*(e**(-x**2-5*x-3)))*(3*x-1)
a = 0.5
b = 1
print("func: " + str(f17))
sum, func = simpson(f17, a, b, 6)
print("\nResult:\nintegrate " + str(f17) + " dx from x=" + str(a) + " to " + str(b) + " = \n" + func + " =\n = " + str(sum))

"""