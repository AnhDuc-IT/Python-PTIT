from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(2, n - 6):
            if Prime(i) and (Prime(i + 2) or Prime(i + 4)) and Prime(i + 6):
                cnt += 1
        print(cnt)
