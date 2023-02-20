# https://youtube.com/watch?v=t9QfcFNkG58&feature=shares

import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x <= 0 else 1

def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    sum = np.dot(w_hidden, x)
    out = [act(x) for x in sum]
    out.append(1)
    out = np.array(out)

    sum = np.dot(w_out, out)
    y = act(sum)
    return y
N = int(input("Введите количество рандомных точек: "))
x1 = np.random.random(N)
x2 = (np.random.random(N)*2)-0.5
C1 = [x1, x2]
C3 = []
C4 = []
for i in range(N):
    inputt = (C1[0][i], C1[1][i])
    if (go(inputt)):
        C3.append(inputt)
    else:
        C4.append(inputt)
for i in range(len(C3)):
    plt.scatter(C3[i][0], C3[i][1], s=10, c='blue')
for i in range(len(C4)):
    plt.scatter(C4[i][0], C4[i][1], s=10, c='red')
plt.plot([0.5, -0.5], color="blue")
plt.plot([1.5, 0.5], color="blue")

plt.grid(True)
plt.show()

