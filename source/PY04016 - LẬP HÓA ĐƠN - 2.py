from math import sqrt
from datetime import*
class Customer:
    def __init__(self, ID, name, room, st, en, charge):
        self.__ID = "KH" + format(ID, "02d")
        self.__name = name
        self.__room = room
        self.__st = st
        self.__en = en
        self.__charge = charge
    def getSt(self):
        return self.__st
    def getEn(self):
        return self.__en
    def getRoom(self):
        return self.__room
    def getID(self):
        return self.__ID
    def getName(self):
        return self.__name
    def getCharge(self):
        return self.__charge
    def totalDays(self):
        date1 = datetime.strptime(self.getSt(), "%d/%m/%Y")
        date2 = datetime.strptime(self.getEn(), "%d/%m/%Y")
        return (date2 - date1).days + 1
    def totalPrices(self):
        if self.getRoom()[0] == '1':
            return self.totalDays() * 25 + self.getCharge()
        elif self.getRoom()[0] == '2':
            return self.totalDays() * 34 + self.getCharge()
        elif self.getRoom()[0] == '3':
            return self.totalDays() * 50 + self.getCharge()
        else:
            return self.totalDays() * 80 + self.getCharge()
    def __str__(self):
        return f'{self.getID()} {self.getName()} {self.getRoom()} {self.totalDays()} {self.totalPrices()}'
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        a = Customer(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input()))
        arr.append(a)
    arr.sort(key = lambda x : x.totalPrices(), reverse= True)
    for x in arr:
        print(x)