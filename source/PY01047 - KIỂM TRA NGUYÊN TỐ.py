from math import*
def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        temp = 0
        for i in range(4):
            temp = temp * 10 + n % 10
            n //= 10
        ans = 0
        while temp > 0:
            ans = ans * 10 + temp % 10
            temp //= 10
        if(check(ans)): print("YES")
        else: print("NO")