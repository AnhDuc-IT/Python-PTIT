from math import*
def check(s):
    if(s[len(s) - 1] == '6' and s[len(s) - 2] == '8'): return "YES"
    return "NO"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(check(s))
        t -=1
