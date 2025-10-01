from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    dem = [0] * 10
    for i in range(len(n) - 2):
        if n[i] != n[i + 2]: return False
        dem[int(n[i])] += 1
    dem[int(n[len(n) - 1])] += 1
    dem[int(n[len(n) - 2])] += 1
    cnt = 0
    for i in range(10):
        if dem[i] != 0:
            cnt += 1
    return cnt == 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")