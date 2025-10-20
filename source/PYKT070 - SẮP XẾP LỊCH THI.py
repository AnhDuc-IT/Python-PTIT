class Subject:
    def __init__(self, id, nameSubject, method):
        self.id = id
        self.nameSubject = nameSubject
        self.method = method
class Exam:
    def __init__(self, code, date, time, room):
        self.code = 'C' + format(code, "03d")
        self.date = date
        self.time = time
        self.room = room
    def getTime(self):
        s = ""
        a = self.date.split("/")
        for x in a:
            s = x + s
        return s
class Calender:
    def __init__(self, Subject, Exam, idGroup, quantity):
        self.Subject = Subject
        self.Exam = Exam 
        self.idGroup = idGroup
        self.quantity = quantity
    def __str__(self):
        return f'{self.Exam.date} {self.Exam.time} {self.Exam.room} {self.Subject.nameSubject} {self.idGroup} {self.quantity}'
if __name__ == "__main__":
    mp = dict()
    mapp = dict()
    file1 = open("MONTHI.in", "r")
    file2 = open("CATHI.in", "r")
    file3 = open("LICHTHI.in", "r")

    n = int(file1.readline().strip())
    for i in range(n):
        a = Subject(file1.readline().strip(), file1.readline().strip(), file1.readline().strip())
        mp[a.id] = a

    m = int(file2.readline().strip())
    for i in range(m):
        a = Exam(i + 1, file2.readline().strip(), file2.readline().strip(), file2.readline().strip())
        mapp[a.code] = a
    arr = []
    p = int(file3.readline().strip())
    for i in range(p):
        s = file3.readline().split()
        a = Calender(mp[s[1]], mapp[s[0]], s[2], s[3])
        arr.append(a)
    arr.sort(key = lambda x : (x.Exam.getTime(), x.Exam.date, x.Exam.code))
    for x in arr:
        print(x)