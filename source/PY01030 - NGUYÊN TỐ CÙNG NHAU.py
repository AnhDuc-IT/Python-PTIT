from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == "__main__":
    n, k = map(int, input().split())
    cnt = 0
    for i in range(10 ** k):
        if(gcd(i, n) == 1 and len(str(i)) == k):
            print(i, end = " ")
            cnt += 1
            if cnt % 10 == 0:
                print("")
