from math import *
class Student:
    def __init__(self, id, name, sc1, sc2, sc3):
        self.id = 'SV' + format(id, "02d")
        self.name = name
        self.sc1 = sc1
        self.sc2 = sc2
        self.sc3 = sc3
    def setName(self):
        a = self.name.split()
        res = ""
        for x in a:
            res += x[0].upper()
            for i in range(1, len(x)):
                res += x[i].lower()
            res += " "
        self.name = res.strip()
    def getScore(self):
        return (3 * self.sc1 + 3 * self.sc2 + 2 * self.sc3) / 8
    def __str__(self):
        return f'{self.id} {self.name} {ceil(self.getScore() * 100) / 100:.2f}'
if __name__ == "__main__":
    n = int(input())
    arr = []
    mp = dict()
    brr = []
    for i in range(1, n + 1):
        a = Student(i, input(), float(input()), float(input()), float(input()))
        a.setName()
        arr.append(a)
        brr.append(a)
    brr.sort(key = lambda x : -x.getScore())
    mp[brr[0].id] = 1
    rank = 1
    for i in range(1, n):
        if(brr[i].getScore() < brr[i - 1].getScore()):
            mp[brr[i].id] = rank + 1
        else:
            mp[brr[i].id] = mp[brr[i - 1].id]
        rank += 1
    for x in brr:
        print(x, mp[x.id])