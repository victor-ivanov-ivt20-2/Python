class Factorial():
    def __init__(self) -> None:
        pass
    def For(self, n):
        if (n < 0):
            return float('inf')
        answer = 1
        for i in range(2, n + 1):
            answer *= i
        return answer
    def While(self, n):
        if (n < 0):
            return float('inf')
        answer = 1
        i = 2
        while (i <= n):
            answer *= i
            i += 1
        return answer