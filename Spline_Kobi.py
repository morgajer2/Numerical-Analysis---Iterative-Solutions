from math import pi

import jacobi_gauss
from sympy import *

x = Symbol('x')


def natural_spline_kobi(f, x0):
    h = list()
    for i in range(len(f) - 1):
        h.append(f[i + 1][0] - f[i][0])

    g = list()
    g.append(0)  # g0
    for i in range(1, len(f) - 1):
        g.append(h[i] / (h[i] + h[i - 1]))
    g.append(0)  # gn

    m = list()
    m.append(0)
    for i in range(1, len(f)):
        m.append(1 - g[i])

    d = list()
    d.append(0)  # d0=0
    for i in range(1, len(f) - 1):
        d.append((6 / (h[i - 1] + h[i])) * (((f[i + 1][1] - f[i][1]) / h[i]) - ((f[i][1] - f[i - 1][1]) / h[i - 1])))
    d.append(0)  # dn

    # building the matrix
    mat = list()

    # first row
    mat.append(list())
    mat[0].append(2)
    for j in range(len(f) - 1):
        mat[0].append(0)

    for i in range(1, len(f) - 1):
        mat.append(list())
        for j in range(len(f)):
            if j == i - 1:  # put miu
                mat[i].append(m[i])
            elif j == i:
                mat[i].append(2)
            elif j == i + 1:  # put lambda
                mat[i].append(g[i])
            else:
                mat[i].append(0)

    # last row
    mat.append(list())
    for j in range(len(f) - 1):
        mat[len(f) - 1].append(0)
    mat[len(f) - 1].append(2)

    print("matrix: " + str(mat))
    print("vector b: " + str(d))

    # get m vector
    print("\nJacobi middle results: ")
    M = (jacobi_gauss.Jacobi(mat, d))
    print("\nvector M: " + str(list(map(float, M))))

    # find S:
    for loc in range(1, len(f)):
        s = (((f[loc][0] - x) ** 3) * M[loc - 1] + ((x - f[loc - 1][0]) ** 3) * M[loc]) / (6 * h[loc - 1])
        s += (((f[loc][0] - x) * f[loc - 1][1]) + ((x - f[loc - 1][0]) * f[loc][1])) / h[loc - 1]
        s -= (((f[loc][0] - x) * M[loc - 1] + (x - f[loc - 1][0]) * M[loc]) * h[loc - 1]) / 6
        print("s" + str(loc - 1) + "(x) = " + str(s))

    # find the location of x0:
    loc = 0
    for i in range(1, len(f)):
        if x0 < f[i][0] and x0 > f[i - 1][0]:
            loc = i
            break

    if loc == 0:
        print("no range found for x0")
        return

    s = (((f[loc][0] - x) ** 3) * M[loc - 1] + ((x - f[loc - 1][0]) ** 3) * M[loc]) / (6 * h[loc - 1])
    s += (((f[loc][0] - x) * f[loc - 1][1]) + ((x - f[loc - 1][0]) * f[loc][1])) / h[loc - 1]
    s -= (((f[loc][0] - x) * M[loc - 1] + (x - f[loc - 1][0]) * M[loc]) * h[loc - 1]) / 6

    print("\nx0 between f(x" + str(loc - 1) + ") = " + str(f[loc - 1][0]) + " and f(x" + str(loc) + ") = " + str(
        f[loc][0]) + " so:")
    print("s" + str(loc - 1) + "(" + str(x0) + ") = " + str(float(s.subs(x, x0))))


"""
# test (from anat):
f = [(0, 0), (pi / 6, 0.5), (pi / 4, 0.7072), (pi / 2, 1)]
x0 = pi / 3
"""

f = [(0, 10), (0.5, 8), (1, 5), (2, 2), (3, 1)]
x0 = 0.75
print("func: " + str(f))
print("x0 = " + str(x0) + "\n")
natural_spline_kobi(f, x0)
