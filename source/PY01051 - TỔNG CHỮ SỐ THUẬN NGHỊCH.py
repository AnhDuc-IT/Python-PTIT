from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    if(len(n) <= 1): return False
    l, r = 0, len(n) - 1
    while l < r:
        if(n[l] != n[r]): return False
        l += 1
        r -= 1
    return True
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = 0
        while n > 0:
            ans += n % 10
            n //= 10
        if(check(str(ans))): print("YES")
        else: print("NO")