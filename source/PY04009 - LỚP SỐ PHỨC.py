class ComplexNums:
    def __init__(self, thuc, ao):
        self.thuc = thuc 
        self.ao = ao
    def __add__(self, other):
        thuc = self.thuc + other.thuc
        ao = self.ao + other.ao
        return ComplexNums(thuc, ao)
    def __mul__(self, other):
        thuc = self.thuc * other.thuc - self.ao * other.ao
        ao = self.thuc * other.ao + self.ao * other.thuc
        return ComplexNums(thuc, ao)
    def __str__(self):
        if self.ao < 0:
            return f'{self.thuc} - {abs(self.ao)}i'
        else:
            return f'{self.thuc} + {self.ao}i'

if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int ,input().split()))
        a = ComplexNums(arr[0], arr[1])
        b = ComplexNums(arr[2], arr[3])
        c = (a + b) * a 
        d = (a + b) * (a + b)
        print(c, ", ", d, sep = "")