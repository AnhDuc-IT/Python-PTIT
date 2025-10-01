from math import*
from collections import Counter
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = []
        while(len(a) < n):
            a += list(map(int, input().split()))
        max_ans = -1e9
        index = 0
        for i in range(len(a)):
            if a[i] > max_ans:
                max_ans = a[i]
                index = i
        a.insert(index, m)
        for x in a:
            if x < 0:
                print(x, end = " ")
        for x in a:
            if x >= 0:
                print(x, end = " ")
        print()