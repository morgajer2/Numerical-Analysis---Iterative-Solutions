import math
import sympy as sp


def evaluate_error(start_point, end_point, eps):
    return math.ceil(-(math.log(eps / (end_point - start_point), math.e)) / math.log(2, math.e))


def Bisection_Method(poli, start_point, end_point, eps):
    """
    a func that finds roots if exists in [start,end] when f(start)*f(end)<0
    :param poli: the polinom
    :param start_point: start
    :param end_point: end
    :param eps: the error
    :return: the root if exists else False
    """
    max_iter = evaluate_error(start_point, end_point, eps)
    count = 0
    c = (start_point + end_point) / 2
    while True:
        if f(poli, start_point) * f(poli, c) < 0:
            end_point = c
        else:
            start_point = c
        last_c = c
        c = (start_point + end_point) / 2
        if max_iter < count:
            return "h"
        elif abs(c - last_c) < eps:
            return round(c, len(str(eps)))


def f(poli, x):
    """
    calc the f(x)
    :param poli: polinom ,list with the factors x+1 -> [1,1]
    :param x: the value we want to calc f(x)
    :return: f(x)
    """
    size = len(poli) - 1
    sum = 0
    for i in range(size + 1):
        sum += poli[i] * (x ** size)
        size -= 1
    return sum


def derived_f(poli):
    """
    func that calc the derivative of the polinom
    :param poli: polinom ,list with the factors x+1 -> [1,1]
    :return: derivative of the polinom
    """
    size = len(poli) - 1  # the aloft of the derivative
    list_der = list()
    for i in range(size):
        list_der.append(poli[i] * (size))
        size = size - 1
    return list_der


def find_roots(poli, start_point, end_point, num_of_range):
    """
    func that find the roots of the func with Bisection_Method
    :param poli: polinom ,list with the factors x+1 -> [1,1]
    :param start_point: the start point of the range
    :param end_point: the end point of the range
    :param num_of_range: number of parts that the range will be divide into
    :return: list of roots of the func
    """
    jump = (end_point - start_point) / num_of_range
    a = start_point
    list_root = list()

    # finding odd Multiplication roots
    for i in range(num_of_range):
        ay = f(poli, a)
        by = f(poli, a + jump)
        if ay * by < 0:  # Suspicious root
            root = Bisection_Method(poli, a, a + jump, 0.000001)
            if not isinstance(root, str):
                list_root.append(root)
        a = a + jump
    return list_root


def allRoots(poli, start_point, end_point, num_of_range):
    roots = find_roots(poli, start_point, end_point, num_of_range)
    d_roots = find_roots(derived_f(poli), start_point, end_point, num_of_range)
    for r in d_roots:
        if f(poli, r) == 0:
            roots.append(r)
    return roots


print(allRoots([1, -3, 0, 0], -4.6, 8, 36))
print(allRoots([1, 5, -4], -10, 5, 50))
