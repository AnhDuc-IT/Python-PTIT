from math import*
a = [True]*1000005
def sieve():
    a[0] = a[1] = False
    for i in range(2, isqrt(100005)):
        if(a[i]):
            for j in range(i * i, 1000005, i):
                a[j] = False
if __name__ == "__main__":
    sieve()
    n, x = map(int, input().split())
    print(x, end = " ")
    cnt = 1
    for i in range(2, 100005):
        if(a[i]):
            print(x + i, end = " ")
            x = i + x
            cnt += 1
        if cnt == n + 1:
            break