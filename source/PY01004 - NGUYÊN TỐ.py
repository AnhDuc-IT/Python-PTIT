from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1
def Gcd(a, b):
    return gcd(a, b)
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        cnt = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                cnt += 1
        if(Prime(cnt)):
            print("YES")
        else:
            print("NO")
        t -= 1
