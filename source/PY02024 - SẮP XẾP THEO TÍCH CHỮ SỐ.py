from functools import cmp_to_key
from math import*
def res(n):
    ans = 1
    while n != 0:
        ans *= n % 10
        n //= 10
    return ans
def cmp(a, b):
    if(res(a) == res(b)):
        return a -  b
    return res(a) - res(b)
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int ,input().split()))
        a.sort(key = cmp_to_key(cmp))
        for x in a:
            print(x, end = " ")
        print()