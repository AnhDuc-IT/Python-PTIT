from math import*
from collections import Counter
def convert(n):
    return int(n, 2)
if __name__ == "__main__":
    s = input()
    if len(s) % 3 == 1:
        s = "00" + s
    if len(s) % 3 == 2:
        s = "0" + s
    res = []
    i = 0
    while(i <= len(s) - 3):
        res.append(convert(s[i:i + 3]))
        i += 3
    for x in res:
        print(x, end = "")