from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000005
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(n):
        if(Prime(a[i]) and cnt[a[i]] > 0):
            print(a[i], cnt[a[i]])
            cnt[a[i]] = 0