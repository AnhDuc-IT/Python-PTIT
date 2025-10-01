from math import*
def check(n):
    if(len(n) < 3): return False
    index =-1
    for i in range(1, len(n)):
        if(int(n[i]) <= int(n[i - 1])):
            index = i - 1
            break
    for i in range(index + 1, len(n)):
        if(int(n[i]) >= int(n[i - 1])): return False
    return True
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if(check(n)): print("YES")
        else: print("NO")