from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        for j in range(n):
            if(j > i and a[j] < a[i]):
                cnt += 1
    print(cnt)