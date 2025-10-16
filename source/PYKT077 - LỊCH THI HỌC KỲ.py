from datetime import datetime

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Test:
    def __init__(self, stt, code, day, hours, group):
        self.stt = 'T' + format(stt, "03d")
        self.code = code
        self.day = day
        self.hours = hours
        self.group = group

    def getDays(self):
        return datetime.strptime(self.day, "%d/%m/%Y")

    def getTime(self):
        return datetime.strptime(self.hours, "%H:%M")

    def __str__(self):
        return f"{self.stt} {self.code} {self.day} {self.hours} {self.group}"

if __name__ == "__main__":
    n, m = map(int, input().split())
    mp = {}
    for _ in range(n):
        id = input().strip()
        name = input().strip()
        mp[id] = name

    arr = []
    for i in range(m):
        p = input().split()
        arr.append(Test(i + 1, p[0], p[1], p[2], p[3]))

    arr.sort(key=lambda x: (x.getDays(), x.getTime(), x.code))
    for x in arr:
        print(x.stt, x.code, mp[x.code], x.day, x.hours, x.group)
