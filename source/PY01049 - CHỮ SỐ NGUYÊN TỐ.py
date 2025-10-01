from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    cnt = 0
    for i in range(len(n)):
        if(Prime(int(n[i]))): cnt += 1
    ans = len(n) - cnt
    return cnt > ans and Prime(len(n))
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)): print("YES")
        else: print("NO")