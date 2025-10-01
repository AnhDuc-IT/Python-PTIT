from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total % 3 == 0
def result(n):
    res = 1
    while n > 0:
        if n % 10 != 0:
            res *= n % 10
        n //= 10
    return res
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(result(n))