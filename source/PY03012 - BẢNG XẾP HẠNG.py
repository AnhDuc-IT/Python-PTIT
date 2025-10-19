class Student:
    def __init__(self, name, correct, quantity):
        self.name = name
        self.correct = correct
        self.quantity = quantity
    def __str__(self):
        return f'{self.name} {self.correct} {self.quantity}'


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        s = list(map(int, input().split()))
        a = Student(name, s[0], s[1])
        arr.append(a)
    arr.sort(key = lambda x : ( -x.correct, x.quantity, x.name))
    for x in arr:
        print(x)