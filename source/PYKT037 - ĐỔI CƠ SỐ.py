from math import*
from collections import Counter
def Recursion(n, k):
    if n == 0:
        print(0, end = "")
        return
    res = []
    while n > 0:
        s = n % k
        if s < 10:
            res.append(s)
        else:
            res.append(chr(ord('A') + s - 10))
        n //= k
    res = res[::-1]
    for x in res:
        print(x, end = "")
if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        Recursion(n, k)
        print()