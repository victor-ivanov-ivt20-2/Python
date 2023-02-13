def Gauss(n, a, b):
    x = [0]*n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][i] == 0.0:
                return "Нельзя делить на ноль! [" + str(i) + "][" + str(i) + "] = " + str(a[i][i])
            k = a[j][i]/a[i][i]
            for l in range(n):
                a[j][l] = a[j][l] - k * a[i][l]
            b[j] = b[j] - k * b[i]
    x[n - 1] = b[n - 1]/a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    return x