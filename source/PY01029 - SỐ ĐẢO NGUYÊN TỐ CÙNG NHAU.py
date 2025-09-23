from math import*
def check(n):
    m = n[::-1]
    if(gcd(int(n), int(m))) == 1: return True
    return False
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)): print("YES")
        else: print("NO")
