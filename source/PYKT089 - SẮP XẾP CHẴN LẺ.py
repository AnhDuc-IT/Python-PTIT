from email.mime import base
from math import*
if __name__ == "__main__":
    n = int(input())
    a = []
    while(len(a) < n):
        a += list(map(int, input().split()))
    b = [x for x in a if x % 2 == 0]
    c = [x for x in a if x % 2 == 1]
    b.sort()
    c.sort(reverse = True)
    bi, ci = 0, 0
    for i in range(n):
        if a[i] % 2 == 0:
            print(b[bi], end = " ")
            bi += 1
        else:
            print(c[ci], end = " ")
            ci += 1