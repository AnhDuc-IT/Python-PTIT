from math import*
from collections import Counter
if __name__ == "__main__":
    s = input()
    a = []
    for i in range(0, len(s) - 1, 2):
        a.append(s[i:i + 2])
    res = {}
    for x in a:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    for x in res.keys():
        print(x, res[x])