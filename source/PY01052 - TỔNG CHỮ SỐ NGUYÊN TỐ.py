from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        if(Prime(total)): print("YES")
        else: print("NO")