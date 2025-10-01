from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    m = n[::-1]
    if m != n or len(m) % 2 != 0: return False
    for i in range(len(m)):
        if int(m[i]) % 2 != 0: return False
    return True
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(22, n, 2):
            if check(str(i)):
                print(i, end = " ")
        print("")