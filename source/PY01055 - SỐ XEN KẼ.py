from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    if(len(n) % 2 == 0): return False
    if(n[0] == n[1]): return False
    for i in range(2, len(n), 2):
        if(n[i] != n[0]): return False
    return True
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
        n = input()
        if(check(n)): print("YES")
        else: print("NO")