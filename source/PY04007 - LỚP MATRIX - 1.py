class Matrix:
    def __init__(self, a, n, m):
        self.a = a
        self.n = n
        self.m = m
    def change(self):
        return [[a[i][j] for i in range(self.n)] for j in range(self.m)]
    def __mul__(self, other):
        res = [[0] * len(other[0]) for _ in range(self.n)]
        for i in range(self.n):
            for j in range(len(other[0])):
                for k in range(self.m):
                    res[i][j] += self.a[i][k] * other[k][j]
        return res
                
    def solve(self):
        for x in self.a:
            for y in x:
                print(y, end = " ")
            print()
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [list(map(int, input().split())) for _ in range(n)]
        res = Matrix(a, n, m)
        ser = res.change()
        ans = res * ser
        for x in ans:
            for y in x:
                print(y, end = " ")
            print()