class Rain:
    def __init__(self, id, name, st, en, quantity):
        self.id = "T" + format(id, "02d")
        self.name = name
        self.st = st
        self.en = en
        self.quantity = quantity
    def __str__(self):
        return f'{self.id} {self.name}'
    def getQuantity(self):
        return self.quantity
    def getName(self):
        return self.name
    def getTime(self):
        h = int(self.en[:2]) - int(self.st[:2])
        m = int(self.en[3:]) - int(self.st[3:])
        return h * 60 + m      
if __name__ == "__main__":
    n = int(input())
    mp = dict()
    mpp = dict()
    arr = []
    for i in range(1, n + 1):
        a = Rain(i, input(), input(), input(), float(input()))
        arr.append(a)
        if a.getName() in mp.keys():
            mp[a.getName()] += a.getQuantity()
            mpp[a.getName()] += a.getTime()
        else:
            mp[a.getName()] = a.getQuantity()
            mpp[a.getName()] = a.getTime()
    for x in arr:
        if mp[x.getName()] != 0:
            res = mp[x.getName()] * 60 / mpp[x.getName()]
            print(x, "{:.2f}".format(res))
            mp[x.getName()] = 0
        
