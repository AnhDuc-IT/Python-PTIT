from math import*
from collections import Counter
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        check = False
        for i in range(len(a)):
            if a[i] > b[i]:
                check = True
                break
        if check:
            print("NO")
        else:
            print("YES")
        