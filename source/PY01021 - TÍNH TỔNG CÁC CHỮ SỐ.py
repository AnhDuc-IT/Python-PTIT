from math import*
from collections import Counter
def Solution(s):
    res = ""
    total = 0
    for x in s:
        if x.isdigit():
            total += ord(x) - ord('0')
        else:
            res += x
    res = sorted(res)
    res += str(total)
    for x in res:
        print(x, end = "")
if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        Solution(s)
        print()