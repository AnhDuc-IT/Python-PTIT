from decimal import Decimal
from math import*
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __sub__(self, other):
        return Point(self.__x - other.__x, self.__y - other.__y)
    def distance(self, other):
        res = self - other
        res = sqrt((res.__x) ** 2 + (res.__y) ** 2)
        return "{:.4f}".format(res)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
