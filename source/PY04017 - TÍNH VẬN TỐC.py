from math import sqrt
from datetime import*
class Person:
    id = ''
    def __init__(self, name, address, en):
        self.name = name
        self.address = address
        self.en = en
    def getId(self):
        res = ""
        s = self.address.split(" ")
        for x in s:
            res += x[0]
        ss = self.name.split(" ")
        for x in ss:
            res += x[0]
        return res
    def setId(self, id):
        self.id = id
    def getTime(self):
        date1 = datetime.strptime("06:00", "%H:%M")
        date2 = datetime.strptime(self.en, "%H:%M")
        ans = date2 - date1
        return 120 / (ans.total_seconds() / 3600)
    def __str__(self):
        return f'{self.id} {self.name} {self.address} {round(self.getTime())} Km/h'
if __name__ == '__main__':

    n = int(input())
    arr = []
    for i in range(n):
        a = Person(input(), input(), input())
        a.setId(a.getId())
        arr.append(a)
    arr.sort(key = lambda x : x.getTime(), reverse = True)
    for x in arr:
        print(x)