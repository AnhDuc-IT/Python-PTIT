from decimal import Decimal
from math import*
class Student:
    def __init__(self, name, birth, sc1, sc2, sc3):
        self.__name = name
        self.__birth = birth
        self.__sc1 = sc1
        self.__sc2 = sc2
        self.__sc3 = sc3
    def total(self):
        return self.__sc1 + self.__sc2 + self.__sc3
    def __str__(self):
        return f'{self.__name} {self.__birth} {self.total()}'
if __name__ == '__main__':
    a = Student(input(), input(), float(input()), float(input()), float(input()))
    print(a)