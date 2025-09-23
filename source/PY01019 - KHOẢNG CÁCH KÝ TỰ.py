from math import*
def check(s):
    x = s[::-1]
    for i in range(1, len(s)):
        if (abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(x[i]) - ord(x[i - 1]))): return "NO"
    return "YES"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(check(s))
        t -=1
