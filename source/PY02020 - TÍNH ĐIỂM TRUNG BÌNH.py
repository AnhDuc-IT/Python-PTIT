from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    a = list(map(float, input().split()))
    a.sort()
    res = 0
    min_ans = a[0]
    max_ans = a[n - 1]
    cnt = 0
    for i in range(1, n):
        if a[i] != min_ans and a[i] != max_ans:
            res += a[i]
            cnt += 1
    res /= cnt
    print("{:.2f}".format(res))