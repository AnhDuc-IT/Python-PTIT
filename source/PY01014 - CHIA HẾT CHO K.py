from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    a, k, n = map(int, input().split())
    check = True
    temp = (a // k + 1)
    ans = temp * k - a
    while ans + a <= n:
        print(ans, end = " ")
        ans = ans + k
        check = False
    if check:
        print(-1)
