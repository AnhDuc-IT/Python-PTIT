from math import sqrt
class Customer:
    def __init__(self, ID, name, st, en):
        self.__ID = ID
        self.__name = name
        self.__st = st
        self.__en = en
    def getSt(self):
        return self.__st
    def getEn(self):
        return self.__en
    def Process(self):
        h = (int(self.getEn()[:2]) - int(self.getSt()[:2])) * 60
        m = int(self.getEn()[3:5]) - int(self.getSt()[3:5])
        return h + m
    def solve(self):
        h = (int(self.getEn()[:2]) - int(self.getSt()[:2])) * 60
        m = int(self.getEn()[3:5]) - int(self.getSt()[3:5])
        res = (h + m) // 60
        ans = (h + m) - res * 60
        return f'{res} gio {ans} phut'
    def __str__(self):
        return f'{self.__ID}  {self.__name} {self.solve()}'
 
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        a = Customer(input(), input(), input(), input())
        arr.append(a)
    arr.sort(key = lambda x : x.Process() ,reverse=True)
    for x in arr:
        print(x)