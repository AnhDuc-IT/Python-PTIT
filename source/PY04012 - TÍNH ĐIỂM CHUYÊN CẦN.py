from math import sqrt
class Student:
    score = 0
    def __init__(self, ID, name, lop):
        self.__ID = ID
        self.__name = name
        self.__lop = lop
    def __str__(self):
        return f'{self.__ID} {self.__name} {self.__lop} {self.score}'
    def getID(self):
        return self.__ID
    def setScore(self, score):
        self.score = score
def Process(s):
    score = 10
    for x in s:
        if x == 'm':
            score -= 1
        elif x == 'v':
            score -= 2
    if score <= 0:
        return "0 KDDK"
    return score
if __name__ == '__main__':
    n = int(input())
    arr = []
    mp = dict()
    for _ in range(n):
        a = Student(input(), input(), input())
        mp[a.getID()] = a
        arr.append(a)
    for _ in range(n):
        id, score = map(str, input().split())
        res = Process(score)
        mp[id].setScore(res)
    for x in arr:
        print(x)
