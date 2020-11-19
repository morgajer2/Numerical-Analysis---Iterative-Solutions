def checkIfSquare(mat):
    """
    this function checks if the matrixis square.
    :param mat: matrix - type list
    :return: boolean
    """
    rows = len(mat)
    for i in mat:
        if len(i) != rows:
            return False
    return True


def isDDM(m, n):
    """
     check the if given matrix is Diagonally Dominant Matrix or not.
    :param m: the matrix, type list.
    :param n: size of the matrix (nxn)
    :return: boolean
    """
    # for each row
    for i in range(0, n):

        # for each column, finding sum of each row.
        sum1 = 0
        for j in range(0, n):
            sum1 = sum1 + abs(m[i][j])

        # removing the diagonal element.
        sum1 = sum1 - abs(m[i][i])

        # checking if diagonal element is less than sum of non-diagonal element.
        if (abs(m[i][i]) < sum1):
            return False
    return True


def rowSum(row, n, x):
    """
    caculates the rowws sum
    :param row: a single row from the matrix
    :param n: the row's size
    :param x: the x vector with results
    :return: the sum
    """
    sum1 = 0
    for i in range(n):
        sum1 += row[i] * x[i]
    return sum1


def checkResult(result, last_result, n, e):
    """
    checking if the result is accurate enough
    :param result: the most recent result
    :param last_result: the previous result
    :param n: the size of the result vector
    :return: boolean
    """
    for i in range(n):
        if result[i] - last_result[i] > e:
            return False
    return True


def Yaakobi(mat, b):  # mat needs to be a list, example: l1 = [[2,3],[4,5]]
    """
    caculating matrix to find vareables vector accourding to yaakobi's algorithem
    :param mat: the matrix
    :param b: the result vector
    :return: the variables vector
    """
    # input check
    n = len(mat)
    if not checkIfSquare(mat):
        return "matrix is not square"
    if len(b) != n:
        return "b is not in the right size"

    # check if Diagonally Dominant Matrix
    if not isDDM(mat, n):
        return "matrix is not Diagonally Dominant"

    # taking a guess: all zeros
    last_result = list()
    for i in range(n):
        last_result.append(0)

    result = last_result.copy()

    while True:
        for i in range(n):  # for each variable
            result[i] = b[i] - (rowSum(mat[i], n, last_result) - mat[i][i] * last_result[i])
            result[i] /= mat[i][i]


        if checkResult(result, last_result, n, 0.001):
            return result
        last_result = result.copy()


def Gauss_Seidel(mat, b):  # mat needs to be a list, example: l1 = [[2,3],[4,5]]
    """
    caculating matrix to find vareables vector accourding to Gauss–Seidel's algorithem
    :param mat: the matrix
    :param b: the result vector
    :return: the variables vector
    """
    # input check
    n = len(mat)
    if not checkIfSquare(mat):
        return "matrix is not square"
    if len(b) != n:
        return "b is not in the right size"

    # check if Diagonally Dominant Matrix
    if not isDDM(mat, n):
        return "matrix is not Diagonally Dominant"

    # taking a guess: all zeros
    last_result = list()
    for i in range(n):
        last_result.append(0)

    result = last_result.copy()
    updated_result = last_result.copy()

    while True:
        for i in range(n):  # for each variable
            result[i] = b[i] - (rowSum(mat[i], n, updated_result) - mat[i][i] * updated_result[i])
            result[i] /= mat[i][i]
            updated_result[i] = result[i]

        if checkResult(result, last_result, n, 0.001):
            return result
        last_result = result.copy()


l1 = [[3, -1, 1], [0, 1, -1], [1, 1, -2]]
b = [4, -1, -3]

print(Yaakobi(l1, b))
print(Gauss_Seidel(l1, b))
