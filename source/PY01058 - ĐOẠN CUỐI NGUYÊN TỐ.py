from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    total = 0
    for i in range(4):
        total = total * 10 + n % 10
        n //= 10
    ans = 0
    while total > 0:
        ans = ans * 10 + total % 10
        total //= 10
    return Prime(ans)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if(check(n)): print("YES")
        else: print("NO")