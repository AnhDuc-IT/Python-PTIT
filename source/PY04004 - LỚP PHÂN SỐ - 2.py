from decimal import Decimal
from math import*
class Fraction:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    def __add__(self, other):
        self.__tu = self.__tu * other.__mau + self.__mau * other.__tu
        self.__mau = self.__mau * other.__mau
        return Fraction(self.__tu, self.__mau)
    def solve(self, other):
        res = self + other
        res = gcd(self.__tu, self.__mau)
        self.__tu //= res
        self.__mau //= res
        print(self.__tu , "/" , self.__mau, sep ='')
if __name__ == '__main__':
    a = list(map(int, input().split()))
    x = Fraction(a[0], a[1])
    y =Fraction(a[2], a[3])
    x.solve(y)