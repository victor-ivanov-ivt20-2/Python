from gauss import Gauss
from cholesky import Cholesky


def GaussInit():
    GaussN = 3
    GaussA = [
            [1, 2, 1],
            [0, 3, -2],
            [1, 1, -1]
        ]
    GaussB = [4, 8, 4]
    for i in range(GaussN):
        print("|", end="  ")
        for j in range(GaussN):
            print(GaussA[i][j], end="  ")
        print("|", end="  ")
        print(GaussB[i], end="  |\n")
    CustomInput = input(
        "Если хотите ввести свои значения, то отправьте цифру 1: ")
    if (CustomInput == '1'):
        GaussN = int(input("Количество решений для метода Гаусса: "))
        GaussA = []
        GaussB = []
        for i in range(GaussN):
            GaussA1 = []
            for j in range(GaussN):
                GaussA1.append(
                    float(input('['+str(i + 1)+']['+str(j + 1)+'] = ')))
            GaussA.append(GaussA1)
            GaussB.append(float(input("  b[" + str(i + 1) + "] = ")))
    GaussAnswer = Gauss(GaussN, GaussA, GaussB)
    print("Ответ по методу Гаусса:")
    for i in range(len(GaussAnswer)):
        print("x[" + str(i + 1) + "] =", GaussAnswer[i])


def CholeskyInit():
    CholeskyN = 3
    CholeskyA = [
        [81, -45, 45],
        [-45, 50, -15],
        [45, -15, 38]
    ]
    CholeskyB = [531, -460, 193]
    
    for i in range(CholeskyN):
        print("|", end="  ")
        for j in range(CholeskyN):
            print(CholeskyA[i][j], end="  ")
        print("|", end="  ")
        print(CholeskyB[i], end="  |\n")
    CustomInput = input(
        "Если хотите ввести свои значения, то отправьте цифру 1: ")

    if (CustomInput == '1'):
        CholeskyN = int(input("Количество решений для метода Холецкого: "))
        CholeskyA = []
        CholeskyB = []
        for i in range(CholeskyN):
            CholeskyA1 = []
            for j in range(CholeskyN):
                CholeskyA1.append(
                    float(input('['+str(i + 1)+']['+str(j + 1)+'] = ')))
            CholeskyA.append(CholeskyA1)
            CholeskyB.append(float(input("  b[" + str(i + 1) + "] = ")))
    CholeskyAnswer = Gauss(CholeskyN, CholeskyA, CholeskyB)
    print("Ответ по методу Холецкого:")
    for i in range(len(CholeskyAnswer)):
        print("x[" + str(i + 1) + "] =", CholeskyAnswer[i])


ChooseMethod = input("Метод Гаусса - 1\nМетод Холецкого - 2\n\t")
if (int(ChooseMethod) == 1):
    GaussInit()
elif (int(ChooseMethod) == 2):
    CholeskyInit()
