from math import*
from collections import Counter
if __name__ == "__main__":
    s = input().split()
    ss = input().split()
    s = [x.lower() for x in s]
    ss = [x.lower() for x in ss]
    a = sorted(set(s) | set(ss))
    b = sorted(set(s) & set(ss))
    for x in a:
        print(x, end = " ")
    print()
    for x in b:
        print(x, end = " ")