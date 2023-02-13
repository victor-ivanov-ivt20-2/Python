from gauss import Gauss
CustomInput = input("Если хотите ввести свои значения, то отправьте цифру 1: ")
if (CustomInput == '1'):
    GaussN = int(input("Количество решений для метода Гаусса: "))
    GaussA = []
    GaussB = []
    for i in range(GaussN):
        GaussA1 = []
        for j in range(GaussN):
            GaussA1.append(float(input('['+str(i + 1)+']['+str(j + 1)+'] = ')))
        GaussA.append(GaussA1)
        GaussB.append(float(input("  b[" + str(i + 1) + "] = ")))
else:
    GaussN = 3
    GaussA = [
        [1, 2, 1],
        [0, 3, -2],
        [1, 1, -1]
    ]
    GaussB = [4, 8, 4]
GaussAnswer = Gauss(GaussN, GaussA, GaussB)
print("Ответ по методу Гаусса:")
for i in range(len(GaussAnswer)):
    print("x[" + str(i + 1) + "] =", GaussAnswer[i])
