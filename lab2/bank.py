import math as m

class Bank():
    def __init__(self, x, p, y):
        self.x = x
        self.p = p
        self.y = y
    def Solution(self):
        if (self.x <= 0):
            return "Вклад не может быть долгом"
        if (self.x > self.y): 
            return "x > y, что противоречит задаче или же ответ будет: 0 лет"
        if (self.p < 0):
            return "x не может увелчиваться на " + str(self.p) + " процентов"
        p = m.floor((self.p / 100)*self.x)
        if (p == 0):
            return "Настолько малый вклад, что сохраняются только копейки,\n которые по условиям задачи отбрасываются.\n В итоге никогда вклад не составит из " + str(self.x) + " в " + str(self.y)
        answer = m.ceil((self.y - self.x) / p)
        return answer
    def Answer(self):
        answer = self.Solution()
        if (isinstance(answer, str)):
            return answer
        if (answer % 100 > 10 and answer % 100 < 20):
            return str(answer) + " лет"
        if (answer % 10 == 1):
            return str(answer) + " год"
        if (answer % 10 > 1 and answer % 10 < 5):
            return str(answer) + " года"
        return str(answer) + " лет"
        