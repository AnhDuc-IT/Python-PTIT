from math import*
from collections import Counter
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        s = list(dict(Counter(a)).items())
        for x, y in s:
            if(y % 2 == 1):
                print(x)