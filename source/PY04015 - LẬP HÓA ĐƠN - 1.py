class Invoice:
    def __init__(self, id, name, st, en):
        self.id = 'KH' + format(id, "02d")
        self.name = name
        self.st = st
        self.en = en
    def getPrice(self):
        res = self.en - self.st
        if res > 100:
            return int(round((50 * 100 + 50 * 150 + (res - 100) * 200) * 105 / 100))
        elif (res >= 51 and res <= 100):
            return int(round((50 * 100 + (res - 50) * 150) * 103 / 100))
        else:
            return int(round(100 * res * 102 / 100))
    def __str__(self):
        return f'{self.id} {self.name} {int(round(int(self.getPrice())))}'
if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        a = Invoice(_ + 1, input(), int(input()), int(input()))
        arr.append(a)
    arr.sort(key = lambda x : -x.getPrice())
    for x in arr:
        print(x)