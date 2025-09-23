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
        used = [0]*1000005
        n = int(input())
        for i in range(2, n):
            if(check(str(i), n) and used[i] == 0 and used[int(str(i)[::-1])] == 0):
                print(i, str(i)[::-1], end = " ")
                used[i] = 1
        print("")
