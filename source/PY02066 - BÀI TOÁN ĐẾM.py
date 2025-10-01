from math import*
from collections import Counter
if __name__ == "__main__":
    n = int(input())
    a = []
    while(len(a) < n):
        s = list(map(int, input().split()))
        a += s
        res = []
    for i in range(1, a[-1] + 1):
        if i not in a:
            res.append(i)
    if len(res):
        for x in res:
            print(x)
    else:
        print("Excellent!")