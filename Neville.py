def neville(f, x0):
    """
    func that work according to neville's algorithm, fids a value at a given x
    :param f: the table of values known, built as a list of tuples (x,y) by ascending order.
            for ex: f = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
    :param x0: the x to find the value for.
    :return: number -> f(x0)
    """

    p = dict()
    s = list()

    count = 0
    for m in f:
        p[(count, count)] = m[1]  # get only y
        s.append("p[" + str(count) + ", " + str(count) + "] = " + str(m[1]))
        count += 1

    count = 1
    while True:
        for m in range(len(f) - count):
            n = m + count
            p[(m, n)] = ((x0 - f[m][0]) * p[(m + 1, n)] - (x0 - f[n][0]) * p[(m, n - 1)]) / (f[n][0] - f[m][0])
            s.append("P[" + str(m) + ", " + str(n) + "] = ((x - x" + str(m) + ") * P[" + str(m + 1) + ", " + str(
                n) + "] - (x - x" + str(n) + ") * P[" + str(m) + ", " + str(n - 1) + "]) / (x" + str(n) + " - x" + str(
                m) + ")")
        if len(f) - count == 1:
            return p[(0, len(f) - 1)], p, s
        count += 1

"""
x0 = 1.47
f = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
t, p, s = neville(f, x0)

print("P array: ")
count = 0
for i in p:
    print(s[count])
    count += 1
    print(str(i) + "= " + str(p[i]) + "\n")

print("\nResult:")
print("f(" + str(x0) + ") = " + str(t))
"""