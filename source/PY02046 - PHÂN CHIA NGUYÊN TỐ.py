from math import*
from collections import Counter
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    res = sum(b)
    check = True
    for i in range(len(b)):
        s = sum(b[:i + 1])
        if Prime(s) and Prime(res - s):
            print(i)
            check = False
            break
    if check:
        print("NOT FOUND")