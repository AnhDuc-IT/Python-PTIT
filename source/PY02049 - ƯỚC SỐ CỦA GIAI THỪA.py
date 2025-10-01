from math import*
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        cnt = 0
        while(p <= n):
            cnt += n // p
            p *= p
        print(cnt)