from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n, k):
    m = n[::-1]
    if m == n or int(m) >= int(k): return False
    return Prime(int(m)) and Prime(int(n))
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        total = n
        for i in range(1000):
            if(total % 7 == 0):
                print(total)
                break
            else:
                total += int(str(n)[::-1])
                n = total
        if(total % 7 != 0):
            print(-1)