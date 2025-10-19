class Electronic:
    def __init__(self, id, name, device, begin, back):
        self.id = "KH" + format(id, "02d")
        self.name = name
        self.device = device
        self.begin = begin
        self.back = back
    def convert(self):
        res = ''
        a = self.name.split()
        for x in a:
            res += x[0].upper()
            for i in range(1, len(x)):
                res += x[i].lower()
            res += " "
        self.name = res.strip()
    def getLimit(self):
        if self.device == 'A':
            return 100
        elif self.device == 'B':
            return 500
        return 200
    def getPrice(self):
        res = self.back - self.begin
        if res <= self.getLimit():
            return res * 450
        else:
            return self.getLimit() * 450
    def getExceed(self):
        res = self.back - self.begin
        if res <= self.getLimit():
            return 0
        return (res - self.getLimit()) * 1000
    def getVAT(self):
        return self.getExceed() // 20
    def getTotal(self):
        return self.getPrice() + self.getExceed() + self.getVAT()
    def __str__(self):
        return f'{self.id} {self.name} {self.getPrice()} {self.getExceed()} {self.getVAT()} {self.getTotal()}'
    

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        s = list(map(str, input().split()))
        a = Electronic(i + 1, name, s[0], int(s[1]), int(s[2]))
        a.convert()
        arr.append(a)
    arr.sort(key = lambda x : x.getTotal(), reverse = True)
    for x in arr:
        print(x)