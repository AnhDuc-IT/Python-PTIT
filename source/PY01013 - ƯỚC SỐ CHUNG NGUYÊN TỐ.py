from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        temp = gcd(a, b)
        sum = 0
        while temp > 0:
            sum += temp % 10
            temp //= 10
        if(Prime(sum)):
            print("YES")
        else:
            print("NO")
        t -= 1
