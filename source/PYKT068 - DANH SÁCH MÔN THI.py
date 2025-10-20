class Subject:
    def __init__(self, id, name, method):
        self.id = id
        self.name = name
        self.method = method
    def __str__(self):
        return f'{self.id} {self.name} {self.method}'
if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        a = Subject(input(), input(), input())
        arr.append(a)
    arr.sort(key = lambda x : x.id)
    for x in arr:
        print(x)