import math


class Exercise():

    def __init__(self):
        self.answer = "Ответ:"

    def getAllAnswers(self):
        print(self.answer, self.exercise_1(), end="\n\n")
        print(self.answer, self.exercise_2(), end="\n\n")
        answer3 = self.exercise_3()
        print(self.answer, "\nОбъём цилиндра: " + str(answer3['cylinder']),
              "\nОбъём конуса: " + str(answer3['cone']), end="\n\n")
        print(self.answer, self.exercise_4(), end="\n\n")
        answer5 = self.exercise_5()
        print(self.answer, "\nПлощадь грани: " + str(answer5['face']),
              "\nПлощадь полной поверхности куба: " + str(answer5['area']),
              "\nОбъём куба: " + str(answer5['volume']), end="\n\n")
        answer6 = self.exercise_6()
        print(self.answer, "\na^8: " + str(answer6['a8']),
              "\na^10: " + str(answer6['a10']),
              "\na^16: " + str(answer6['a16']), end="\n\n")
    def exercise_1(self):
        print("Задание 1.\n" +
              "Написать программу для сложения двух " +
              "заданных пользователем чисел a и b.")
        print("Введите первое число a: ", end="")
        a = float(input())
        print("Введите второе число b: ", end="")
        b = float(input())
        return a + b

    def exercise_2(self):
        print("Задание 2.\n" +
              "Угол A задан в градусах. " +
              "Найти его величину в радианах.")
        print("Введите угол α: ", end="")
        a = float(input())
        return round(math.radians(a), 4)

    def exercise_3(self):
        print("Задание 3.\n" +
              "Написать программу для вычисления " +
              "объема цилиндра и конуса, " +
              "которые имеют одинаковую высоту H " +
              "и одинаковый радиус основания R.")
        print("Введите высоту H: ", end="")
        h = float(input())
        print("Введите радиус R: ", end="")
        r = float(input())
        cylinder = math.pi * r**2 * h
        answer = {
            'cylinder': round(cylinder, 4),
            'cone': round(cylinder/3, 4)
        }
        return answer

    def exercise_4(self):
        print("Задание 4.\n" +
              "Составить программу вычисления для " +
              "заданного трехзначного целого " +
              "числа произведения его цифр")
        print("Введите трёхзначное число: ", end="")
        x = int(input())
        return (x % 10)*((x % 100)//10)*(x//100)

    def exercise_5(self):
        print("Задание 5.\n" +
              "Дана длина ребра куба. " +
              "Найти площадь грани, площадь полной " +
              "поверхности и объем этого куба.")
        print("Введите длину ребра куба: ", end="")
        a = float(input())
        answer = {
            'face': a*a,
            'area': (a*a)*6,
            'volume': a*a*a
        }
        return answer

    def exercise_6(self):
        print("Задание 6.\n" +
        "Дано действительное число а. " + 
        "Не используя никаких функций и " +
        "никаких операций, кроме умножения, " +
        "получить a^8 за три операции; " +
        "a^10 и a^16 за четыре операции.")
        print("Введите число a: ", end="")
        a = float(input())
        b = a
        c = a
        answer = dict()
        a *= a
        a *= a
        a *= a
        answer['a8'] = a
        b *= b
        b *= b
        b *= c
        b *= b
        answer['a10'] = b
        c *= c
        c *= c
        c *= c
        c *= c
        answer['a16'] = c
        return answer
