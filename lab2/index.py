from factorial import Factorial
from bank import Bank
print("Нахождения факториала через цикл for", end="\n\n")
print("Ответ: ", Factorial().For(int(input("Введите число: "))))
print("======================================")
print("Нахождения факториала через цикл while", end="\n\n")
print("Ответ: ", Factorial().While(int(input("Введите число: "))))
print("======================================")
print("Задание 3", end="\n\n")
print("Ответ: ", Bank(int(input("x: ")), int(input("p: ")), int(input("y: "))).Answer()) 