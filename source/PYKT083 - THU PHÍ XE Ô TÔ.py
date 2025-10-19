class Vehicle:
    def __init__(self, licensePlate, device, seat, go, date):
        self.licensePlate = licensePlate
        self.device = device
        self.seat = seat
        self.go = go
        self.date = date
    def getDate(self):
        return self.date
    def getCharge(self):
        if self.go == 'IN':
            if self.device == 'Xe_con':
                if self.seat == 5:
                    return 10000
                else:
                    return 15000
            elif self.device == 'Xe_tai':
                return 20000
            else:
                if self.seat == 29:
                    return 50000
                else:
                    return 70000
        return 0
def change(s):
    a = s.split("/")
    res = ""
    for x in a:
        res = x + res
    return res
if __name__ == "__main__":
    n = int(input())
    mp = dict()
    arr = set()
    for i in range(n):
        s = list(map(str, input().split()))
        a = Vehicle(s[0], s[1], int(s[2]), s[3], s[4])
        arr.add(a.getDate())
        if a.getDate() in mp:
            mp[a.getDate()] += a.getCharge()
        else:
            mp[a.getDate()] = a.getCharge()
    arr = list(arr)
    arr.sort(key = lambda x : change(x))
    for x in arr:
        print(x,": ",mp[x], sep = "")