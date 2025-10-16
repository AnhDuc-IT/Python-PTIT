class Teacher:
    def __init__(self, id, name, area, s1, s2):
        self.id = "GV" + format(id, "02d")
        self.name = name
        self.area = area
        self.s1 = s1
        self.s2 = s2
    def getPriority(self):
        s = self.area[1]
        if s == '1':
            return 2
        elif s == '2':
            return 1.5
        elif s == '3':
            return 1
        return 0
    def getScore(self):
        return self.s1 * 2 + self.s2 + self.getPriority()
    def getSubject(self):
        s = self.area[0]
        if s == 'A':
            return "TOAN"
        elif s == 'B':
            return "LY"
        return "HOA"
    def getResult(self):
        res = self.getScore()
        if res >= 18:
            return "TRUNG TUYEN"
        else:
            return "LOAI"
    def __str__(self):
        return f'{self.id} {self.name} {self.getSubject()} {self.getScore()} {self.getResult()}'
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        a = Teacher(i + 1, input(), input(), float(input()), float(input()))
        arr.append(a)
    arr.sort(key = lambda x : x.getScore(), reverse = True)
    for x in arr:
        print(x)