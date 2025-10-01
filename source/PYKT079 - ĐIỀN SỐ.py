from math import*
from collections import Counter
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = []
        while(len(a) < n):
            a += list(map(int, input().split()))
        a.sort()
        cnt = a[0]
        res = 0
        for i in range(a[0], a[n - 1] + 1, 1):
            if i not in a:
                res += 1
        print(res)