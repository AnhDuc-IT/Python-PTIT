
class Candidate:
    def __init__(self, id, name, score, race, area):
        self.id = 'TS' + format(id, "02d")
        self.name = name
        self.score = score
        self.race = race
        self.area = area
    def setName(self):
        a = self.name.split()
        res = ""
        for x in a:
            res += x[0].upper()
            for i in range(1, len(x)):
                res += x[i].lower()
            res += " "
        self.name = res
    def getScore(self):
        res = self.score
        if self.race == 'Kinh':
            res += 0
        else:
            res += 1.5
        if self.area == 1:
            res += 1.5
        elif self.area == 2:
            res += 1
        return res
    def getResult(self):
        if self.getScore() >= 20.5:
            return "Do"
        return "Truot"
    def __str__(self):
        return f'{self.id} {self.name} {self.getScore()} {self.getResult()}'
    

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        a = Candidate(i + 1, input(), float(input()), input(), int(input()))
        a.setName()
        arr.append(a)
    arr.sort(key = lambda x : (x.getScore()), reverse=True)
    for x in arr:
        print(x)