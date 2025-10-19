from math import*
nt = [True] * 10005
def sieve():
    global nt
    nt[0] = nt[1] = False
    for i in range(2, isqrt(10001) + 1):
        if nt[i]:
            for j in range(i * i, 10001, i):
                nt[j] = False
if __name__ == "__main__":
    sieve()
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for x in arr:
        if not nt[x]:
            inc, dec = 0, 0
            for i in range(x, 10001):
                if nt[i]:
                    inc = i
                    break
            for i in range(x, 1, -1):
                if nt[i]:
                    dec = i
                    break
            inc = abs(x - inc)
            dec = abs(x - dec)
            res = max(res, min(inc, dec))
    print(res)