class Exam:
    def __init__(self, id, day, time, room):
        self.id = 'C' + format(id, "03d")
        self.day = day
        self.time = time
        self.room = room
    def getDay(self):
        res = ''
        for x in self.day.split("/"):
            res = x + res
        return res
    def __str__(self):
        return f'{self.id} {self.day} {self.time} {self.room}'
if __name__ == "__main__":
    file = open("CATHI.in", "r")
    n = int(file.readline())
    arr = []
    for i in range(n):
        a = Exam(i + 1, file.readline().strip(), file.readline().strip(), file.readline().strip())
        arr.append(a)
    arr.sort(key = lambda x : (x.getDay(), x.time, x.id))
    for x in arr:
        print(x)