from math import*
def Prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    for i in range(len(n)):
        if(not Prime(i)):
            if(Prime(int(n[i]))): return False
        else:
            if(not Prime(int(n[i]))): return False
    return True
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)): print("YES")
        else: print("NO")