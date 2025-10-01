from math import*
from collections import Counter
if __name__ == "__main__":
    a = input()
    b = input()
    p = int(input())
    s = a[:p - 1] + b + a[p - 1:]
    print(s)