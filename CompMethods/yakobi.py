def normal(x0, x1, N):
    x0sum = 0
    x1sum = 0
    for i in range(N):
        x0sum = x0sum + abs(x0[i])
        x1sum = x1sum + abs(x1[i])
    return abs(x1sum - x0sum)


def main():
    N = 3
    A = [[20, -2, 4],
        [3, 10, 1],
        [4, 6, 15]]
    B = [16, 2, -11]
    e = 0.0001
    x0 = [0]*N
    x1 = [1]*N
    
    for i in range(N):
        L = 0
        for j in range(N):
            if (j != i):
                L = L + A[i][j]*x0[j]
            x1[i] = (B[i] - L)/A[i][i]
    while(normal(x0, x1, N) >= e):
        for i in range(N):
            x0[i] = x1[i]
        for i in range(N):
            L = 0
            for j in range(N):
                if (j != i):
                    L = L + A[i][j]*x0[j]
            x1[i] = (B[i] - L)/A[i][i]
    print("Реальные значения: ", end="")
    print(x1)
    print("Округлённые значения до 5 знаков: [", end="")

    for i in range(N):
        if (i + 1 == N):
            print(round(x1[i], 5), end="]")
        else:
            print(round(x1[i], 5), end=", ")


if __name__ == '__main__':
    main()
