from decimal import Decimal
from math import*
class Fraction:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau
    def solve(self):
        res = gcd(self.__tu, self.__mau)
        self.__tu //= res
        self.__mau //= res
        print(self.__tu , "/" , self.__mau, sep ='')
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    a = Fraction(tu, mau)
    a.solve()