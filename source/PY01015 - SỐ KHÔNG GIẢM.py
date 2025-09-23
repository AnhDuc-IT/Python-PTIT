from math import*
def check(s):
    for i in range(len(s) - 1):
        if(s[i] > s[i + 1]): return "NO"
    return "YES"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(check(s))
        t -=1
