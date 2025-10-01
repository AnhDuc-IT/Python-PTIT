from functools import cmp_to_key
from math import*
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if gcd(a[i], a[j]) == 1:
                res.append((a[i], a[j]))
    for x in res:
        for y in x:
            print(y, end = " ")
        print()