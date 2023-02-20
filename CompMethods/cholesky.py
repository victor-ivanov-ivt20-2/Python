import math as m
from gauss import Gauss
def LiteGauss(n, A, b):
    x = [0]*n
    x[n - 1] = b[n - 1]/A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j]*x[j]
        x[i] = x[i]/A[i][i]
    return x
def transpose(n, A):
    L = [[0] * n for i in range(n)]
    for i in range(n):
        L[i][i] = A[i][i]
        for j in range(n - 1, i, -1):
            L[i][j] = A[j][i]
    return L
def Cholesky(n, A, b):
    x = [0]*n
    L = [[0] * n for i in range(n)]
    L[0][0] = m.sqrt(A[0][0])
    for i in range(1, n):
        L[i][0] = A[i][0]/L[0][0]
    for i in range(1, n):
        sum = 0
        for p in range(0, i):
            sum = sum + L[i][p]*L[i][p]
        L[i][i] = m.sqrt(A[i][i] - sum)
        for j in range(i + 1, n):
            sum = 0
            if (i == 1):
                sum = L[i][0] * L[j][0]
            for p in range(0, i - 1):
                sum = sum + (L[i][p] * L[j][p])
            L[j][i] = (A[j][i] - sum)/L[i][i]
    LT = transpose(n, L)
    y = Gauss(n, L, b)
    x = LiteGauss(n, LT, y)
    return x

