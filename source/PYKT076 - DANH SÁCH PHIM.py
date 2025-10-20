class Category:
    def __init__(self, category, types):
        self.category = category
        self.types = 'TL' + format(types, '03d')
class Movie:
    def __init__(self, id, code, day, name, series, Category):
        self.id = 'P' + format(id, "03d")
        self.code = code
        self.day = day
        self.name = name
        self.series = series
        self.Category = Category
    def getDays(self):
        res = ''
        for x in self.day.split("/"):
            res = x + res
        return res
    def __str__(self):
        return f'{self.id} {self.Category.category} {self.day} {self.name} {self.series}'
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    mp = dict()
    for i in range(n):
        a = Category(input(), i + 1)
        mp[a.types] = a
    for i in range(m):
        code = input()
        day = input()
        name = input()
        series = int(input())
        a = Movie(i + 1, code, day, name, series, mp[code])
        arr.append(a)
    arr.sort(key = lambda x : (x.getDays(), x.name, -x.series))
    for x in arr:
        print(x)