from math import *
class Employee:
    def __init__(self, code, name, salary, days):
        self.code = code
        self.name = name
        self.salary = salary
        self.days = days
    def getYeas(self):
        return int(self.code[1:3])
    def getHeSo(self):
        s = self.code[0]
        ss = self.getYeas()
        if s == 'A':
            if ss <= 3:
                return 10
            elif ss <= 8:
                return 12
            elif ss <= 15:
                return 14
            else:
                return 20
        elif s == 'B':
            if ss <= 3:
                return 10
            elif ss <= 8:
                return 11
            elif ss <= 15:
                return 13
            else:
                return 16
        elif s == 'C':
            if ss <= 3:
                return 9
            elif ss <= 8:
                return 10
            elif ss <= 15:
                return 12
            else:
                return 14
        else:
            if ss <= 3:
                return 8
            elif ss <= 8:
                return 9
            elif ss <= 15:
                return 11
            else:
                return 13
    def getId(self):
        return self.code[3:]
    def getSalary(self):
        return self.salary * self.days * self.getHeSo() * 1000
if __name__ == "__main__":
    n = int(input())
    mp = dict()
    for i in range(n):
        a = input()
        mp[a[:2]] = a[3:]
    m = int(input())
    arr = []
    for i in range(m):
        a = Employee(input(), input(), int(input()), int(input()))
        arr.append(a)
    for x in arr:
        print(x.code, x.name, mp[x.getId()], x.getSalary())