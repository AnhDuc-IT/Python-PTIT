class Team:
    def __init__(self, id, name, school):
        self.id = "Team" + format(id, "02d")
        self.name = name
        self.school = school
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getSchool(self):
        return self.school
class Candidate:
    def __init__(self, code, fullName, team):
        self.code = "C" + format(code, "03d")
        self.fullName = fullName
        self.team = team
    def getFullName(self):
        return self.fullName
    def getTeam(self):
        return self.team
    def __str__(self):
        return f'{self.code} {self.fullName}'
if __name__ == "__main__":
    n = int(input())
    mp = dict()
    arr = []
    for i in range(n):
        a = Team(i + 1, input(), input())
        mp[a.getId()] = a
    m = int(input())
    for i in range(m):
        a = Candidate(i + 1, input(), input())
        arr.append(a)
    arr.sort(key = lambda x : x.getFullName())
    for x in arr:
        print(x, mp[x.getTeam()].getName(), mp[x.getTeam()].getSchool())
