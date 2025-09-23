from math import*
def check(n):
    for i in range(len(n)):
        if(n[i] != '4' and n[i] != '7'): return False
    return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1
