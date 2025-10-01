from functools import cmp_to_key
from math import*
a = []
k = 0
check = True
n = 0
def ktao():
    global a
    a = list(range(k))
def Generate():
    global a, check
    i = k - 1
    while i >= 0 and a[i] == n - k + i:
        i -= 1
    if i < 0:
        check = False
    else:
        a[i] += 1
        for j in range(i + 1, k):
            a[j] = a[j - 1] + 1
if __name__ == "__main__":
    n, k = map(int, input().split())
    se = set(map(int, input().split()))
    arr = sorted(list(se))
    n = len(arr)
    ktao()
    check = True
    while check == True:
        for i in range(k):
            print(arr[a[i]], end = " ")
        print()
        Generate()