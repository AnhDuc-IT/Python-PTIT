from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == "__main__":
    l, r = map(int ,input().split())
    for i in range(l, r - 1):
        for j in range(i + 1, r):
            for k in range(j + 1, r + 1):
                if(gcd(j, i) == 1 and gcd(j, k) == 1 and gcd(i, k) == 1):
                    print("(",i, ", ", j, ", ", k, ")", sep = "")
