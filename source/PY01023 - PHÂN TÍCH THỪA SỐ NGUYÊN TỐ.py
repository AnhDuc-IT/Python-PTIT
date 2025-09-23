from math import*
def check(s):
    x = s[::-1]
    for i in range(1, len(s)):
        if (abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(x[i]) - ord(x[i - 1]))): return "NO"
    return "YES"
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        print(1, end = "")
        for i in range(2, isqrt(n) + 1):
            if(n % i == 0):
                cnt = 0
                while(n % i == 0):
                    cnt += 1
                    n //= i
                print(" * ", i, "^", cnt, end = "", sep = "")
        if(n > 1): print(" * ",n, "^1", end = "", sep = "")
        print("\n")
        t -=1
