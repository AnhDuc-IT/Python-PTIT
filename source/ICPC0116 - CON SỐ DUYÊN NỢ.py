from math import*
def check(n):
    return n[0] == n[len(n) - 1]
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = (input())
        if(check(n)): print("YES")
        else: print("NO")
