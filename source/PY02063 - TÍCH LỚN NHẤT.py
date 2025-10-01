from math import*
from collections import Counter
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[0] * a[1] * a[n - 1]
    c = a[n - 1] * a[n - 2] * a[n - 3]
    d = a[0] * a[1] * a[2]
    c = max(c, d)
    b = max(c, b)
    print(b)